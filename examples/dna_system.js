// 🧬 Conceito: Sistema de DNA Digital
// AVISO: Este é um exemplo conceitual, não código em produção

/**
 * Inspiração: Genética e herança cultural
 * - Características são herdadas mas também evoluem
 * - Cada "geração" mantém essência e adapta ao contexto
 * - Mudanças podem ser revertidas se necessário
 */

class DigitalDNA {
  constructor(parentDNA = null) {
    this.id = this.generateId();
    this.parentDNA = parentDNA;
    this.generation = parentDNA ? parentDNA.generation + 1 : 0;
    this.preferences = this.inheritPreferences(parentDNA);
    this.changes = []; // histórico de mudanças
    this.createdAt = new Date();
  }

  inheritPreferences(parentDNA) {
    // Valores padrão para novos usuários
    const defaultPreferences = {
      theme: 'light',
      layout: 'simple',
      privacy: 'balanced',
      helpfulness: 0.5 // 0 = nunca ajuda, 1 = sempre ajuda
    };

    if (!parentDNA) {
      return defaultPreferences;
    }

    // Herda preferências do "pai" com pequenas variações
    return {
      theme: this.mutatePreference(parentDNA.preferences.theme, ['light', 'dark', 'auto']),
      layout: this.mutatePreference(parentDNA.preferences.layout, ['simple', 'detailed', 'minimal']),
      privacy: parentDNA.preferences.privacy, // privacy não muda na herança
      helpfulness: Math.max(0, Math.min(1, parentDNA.preferences.helpfulness + (Math.random() - 0.5) * 0.1))
    };
  }

  mutatePreference(current, options) {
    // 80% chance de manter preferência atual
    // 20% chance de mudar para opção relacionada
    return Math.random() < 0.8 ? current : options[Math.floor(Math.random() * options.length)];
  }

  // Evolui baseado no comportamento real do usuário
  evolveBasedOnBehavior(interactions) {
    interactions.forEach(interaction => {
      switch (interaction.type) {
        case 'theme_change':
          this.updatePreference('theme', interaction.value);
          break;
        case 'helped_someone':
          this.updatePreference('helpfulness', Math.min(1, this.preferences.helpfulness + 0.01));
          break;
        case 'requested_help':
          // Não muda helpfulness - pedir ajuda é normal
          break;
        case 'privacy_change':
          this.updatePreference('privacy', interaction.value);
          break;
      }
    });
  }

  updatePreference(key, value) {
    const oldValue = this.preferences[key];
    this.preferences[key] = value;
    
    // Registra mudança para possível rollback
    this.changes.push({
      timestamp: new Date(),
      key,
      oldValue,
      newValue: value
    });
  }

  // Permite voltar a estados anteriores
  rollback(targetTimestamp) {
    const relevantChanges = this.changes.filter(change => 
      change.timestamp > targetTimestamp
    );

    // Reverte mudanças na ordem inversa
    relevantChanges.reverse().forEach(change => {
      this.preferences[change.key] = change.oldValue;
    });

    // Remove mudanças revertidas do histórico
    this.changes = this.changes.filter(change => 
      change.timestamp <= targetTimestamp
    );
  }

  // Gera interface baseada nas preferências
  generateInterface() {
    return {
      theme: this.preferences.theme,
      layout: this.preferences.layout,
      privacyControls: this.generatePrivacyControls(),
      helpingFeatures: this.generateHelpingFeatures()
    };
  }

  generatePrivacyControls() {
    const controls = {
      'open': ['Share everything', 'Public profile', 'Open messaging'],
      'balanced': ['Share basics', 'Selective sharing', 'Friend requests'],
      'private': ['Minimal sharing', 'Anonymous mode', 'No tracking']
    };

    return controls[this.preferences.privacy] || controls['balanced'];
  }

  generateHelpingFeatures() {
    const helpfulness = this.preferences.helpfulness;
    
    if (helpfulness > 0.7) {
      return ['Actively offer help', 'Mentor newcomers', 'Community leadership'];
    } else if (helpfulness > 0.3) {
      return ['Respond to requests', 'Participate in discussions', 'Share knowledge'];
    } else {
      return ['Observe community', 'Learn from others', 'Gradual participation'];
    }
  }

  // Cria "filho" para convite
  createChild() {
    return new DigitalDNA(this);
  }

  // Relatório sobre estado atual
  generateReport() {
    return {
      id: this.id,
      generation: this.generation,
      age: Date.now() - this.createdAt.getTime(),
      preferences: this.preferences,
      changes: this.changes.length,
      interface: this.generateInterface()
    };
  }

  // Utilitário para gerar IDs únicos
  generateId() {
    return Date.now().toString(36) + Math.random().toString(36).substr(2);
  }
}

// ⚠️ LIMITAÇÕES CONHECIDAS:
// - Preferências podem não refletir necessidades reais
// - Mutações podem gerar resultados inesperados
// - Rollback pode confundir usuários
// - Sistema pode ser manipulado por usuários experientes

// 🧪 Exemplo de uso (conceitual)
function demonstrateSystem() {
  // Usuário original
  const originalUser = new DigitalDNA();
  console.log('Usuário original:', originalUser.generateReport());

  // Usuário convidado herda características
  const invitedUser = originalUser.createChild();
  console.log('Usuário convidado:', invitedUser.generateReport());

  // Simulação de comportamento
  invitedUser.evolveBasedOnBehavior([
    { type: 'theme_change', value: 'dark' },
    { type: 'helped_someone', value: true },
    { type: 'helped_someone', value: true }
  ]);

  console.log('Após interações:', invitedUser.generateReport());

  // Rollback se necessário
  const oneMinuteAgo = new Date(Date.now() - 60000);
  invitedUser.rollback(oneMinuteAgo);
  console.log('Após rollback:', invitedUser.generateReport());
}

// Apenas execute se este arquivo for rodado diretamente
if (typeof module !== 'undefined' && require.main === module) {
  demonstrateSystem();
}

// NOTA: Este código é experimental e pode mudar completamente
// baseado em feedback de usuários reais e descobertas técnicas

export { DigitalDNA };