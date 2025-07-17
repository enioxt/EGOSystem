// 🤝 Exemplo: Sistema de Autorregulação Comunitária

class CommunityRegulation {
  constructor() {
    this.users = new Map();
    this.interactions = [];
    this.communityFeedback = [];
  }

  // 📊 Sistema de Reputação Transparente
  calculateReputation(userId) {
    const userActions = this.interactions.filter(i => i.userId === userId);
    
    const contributions = userActions.filter(a => a.type === 'contribution');
    const extractions = userActions.filter(a => a.type === 'extraction');
    const helpGiven = userActions.filter(a => a.type === 'help_given');
    const helpReceived = userActions.filter(a => a.type === 'help_received');
    const communityFeedback = this.communityFeedback.filter(f => f.targetUserId === userId);

    const reputation = {
      userId,
      contributionScore: contributions.length,
      extractionScore: extractions.length,
      helpBalance: helpGiven.length - helpReceived.length,
      communityRating: this.calculateCommunityRating(communityFeedback),
      giveToTakeRatio: this.calculateGiveToTakeRatio(contributions, extractions),
      overallScore: 0,
      status: 'neutral',
      visibility: 'public' // Sempre transparente
    };

    // Cálculo do score geral
    reputation.overallScore = this.calculateOverallScore(reputation);
    reputation.status = this.determineStatus(reputation.overallScore);

    return reputation;
  }

  calculateCommunityRating(feedback) {
    if (feedback.length === 0) return 0.5; // Neutro para novos usuários
    
    const positiveCount = feedback.filter(f => f.rating > 0.5).length;
    const negativeCount = feedback.filter(f => f.rating < 0.5).length;
    
    return positiveCount / (positiveCount + negativeCount);
  }

  calculateGiveToTakeRatio(contributions, extractions) {
    if (extractions.length === 0) return contributions.length > 0 ? Infinity : 1;
    return contributions.length / extractions.length;
  }

  calculateOverallScore(reputation) {
    const weights = {
      giveToTakeRatio: 0.4,
      helpBalance: 0.3,
      communityRating: 0.3
    };

    let score = 0;
    
    // Ratio de dar vs receber (normalizado)
    const normalizedRatio = Math.min(reputation.giveToTakeRatio, 5) / 5;
    score += normalizedRatio * weights.giveToTakeRatio;
    
    // Balanço de ajuda (normalizado)
    const normalizedBalance = Math.max(0, Math.min(reputation.helpBalance + 10, 20)) / 20;
    score += normalizedBalance * weights.helpBalance;
    
    // Rating da comunidade
    score += reputation.communityRating * weights.communityRating;
    
    return score;
  }

  determineStatus(score) {
    if (score >= 0.8) return 'exemplary';
    if (score >= 0.6) return 'good';
    if (score >= 0.4) return 'neutral';
    if (score >= 0.2) return 'concerning';
    return 'problematic';
  }

  // 🚨 Identificação de Comportamentos Problemáticos
  identifyProblematicBehavior(userId) {
    const reputation = this.calculateReputation(userId);
    const userActions = this.interactions.filter(i => i.userId === userId);
    
    const issues = [];

    // Usuário Parasita
    if (reputation.giveToTakeRatio < 0.2) {
      issues.push({
        type: 'parasitic',
        severity: 'high',
        description: 'Extrai muito mais do que contribui',
        evidence: {
          contributions: reputation.contributionScore,
          extractions: reputation.extractionScore,
          ratio: reputation.giveToTakeRatio
        }
      });
    }

    // Usuário Egoísta
    if (reputation.helpBalance < -5) {
      issues.push({
        type: 'selfish',
        severity: 'medium',
        description: 'Recebe muito mais ajuda do que oferece',
        evidence: {
          helpBalance: reputation.helpBalance
        }
      });
    }

    // Baixa avaliação da comunidade
    if (reputation.communityRating < 0.3) {
      issues.push({
        type: 'community_rejection',
        severity: 'high',
        description: 'Comunidade avalia negativamente',
        evidence: {
          rating: reputation.communityRating
        }
      });
    }

    return {
      userId,
      issues,
      overallSeverity: this.calculateOverallSeverity(issues),
      recommendedActions: this.generateRecommendedActions(issues)
    };
  }

  calculateOverallSeverity(issues) {
    const severityScores = { low: 1, medium: 2, high: 3 };
    const totalScore = issues.reduce((sum, issue) => sum + severityScores[issue.severity], 0);
    
    if (totalScore >= 6) return 'critical';
    if (totalScore >= 4) return 'high';
    if (totalScore >= 2) return 'medium';
    return 'low';
  }

  generateRecommendedActions(issues) {
    const actions = [];
    
    issues.forEach(issue => {
      switch (issue.type) {
        case 'parasitic':
          actions.push('Reduzir visibilidade das postagens do usuário');
          actions.push('Limitar acesso a recursos premium');
          actions.push('Sugerir formas de contribuição');
          break;
        case 'selfish':
          actions.push('Incentivar oferecimento de ajuda');
          actions.push('Conectar com oportunidades de mentoria');
          break;
        case 'community_rejection':
          actions.push('Facilitar diálogo com a comunidade');
          actions.push('Oferecer orientação sobre comportamento');
          break;
      }
    });

    return [...new Set(actions)]; // Remove duplicatas
  }

  // 🔄 Respostas Graduais da Comunidade
  applyCommunityResponse(userId, severity) {
    const responses = {
      low: [
        'Feedback sutil através de menos engajamento',
        'Redução gradual de convites para colaborações'
      ],
      medium: [
        'Conversas diretas sobre comportamento',
        'Redução de visibilidade nas feeds',
        'Menos oportunidades de liderança'
      ],
      high: [
        'Isolamento parcial de grupos',
        'Perda de privilégios especiais',
        'Feedback direto da comunidade'
      ],
      critical: [
        'Isolamento quase completo',
        'Perda de acesso a recursos avançados',
        'Consideração de banimento comunitário'
      ]
    };

    return {
      userId,
      severity,
      actions: responses[severity],
      timeline: this.generateTimeline(severity),
      reversible: true,
      communityVote: severity === 'critical' ? 'required' : 'optional'
    };
  }

  generateTimeline(severity) {
    const timelines = {
      low: '1-2 semanas',
      medium: '2-4 semanas',
      high: '1-2 meses',
      critical: '3-6 meses ou permanente'
    };
    
    return timelines[severity];
  }

  // 🌟 Sistema de Reconhecimento Positivo
  recognizePositiveBehavior(userId) {
    const reputation = this.calculateReputation(userId);
    
    if (reputation.status === 'exemplary') {
      return {
        userId,
        recognitions: [
          'Destaque na página principal',
          'Convites para liderar projetos',
          'Acesso a recursos exclusivos',
          'Voz amplificada na comunidade',
          'Mentoria de novos usuários'
        ],
        benefits: [
          'Maior visibilidade',
          'Mais oportunidades',
          'Reconhecimento público',
          'Influência na governança'
        ]
      };
    }
    
    return null;
  }

  // 📈 Simulação de Cenários
  simulateScenario(scenarioName) {
    const scenarios = {
      'parasitic_user': {
        description: 'Usuário que só extrai valor sem contribuir',
        actions: [
          { type: 'extraction', count: 20 },
          { type: 'contribution', count: 1 },
          { type: 'help_received', count: 15 },
          { type: 'help_given', count: 0 }
        ],
        expectedOutcome: 'Isolamento gradual da comunidade'
      },
      
      'generous_contributor': {
        description: 'Usuário que sempre ajuda e contribui',
        actions: [
          { type: 'contribution', count: 25 },
          { type: 'extraction', count: 5 },
          { type: 'help_given', count: 30 },
          { type: 'help_received', count: 8 }
        ],
        expectedOutcome: 'Reconhecimento e liderança natural'
      },
      
      'balanced_user': {
        description: 'Usuário equilibrado que contribui e recebe',
        actions: [
          { type: 'contribution', count: 12 },
          { type: 'extraction', count: 10 },
          { type: 'help_given', count: 15 },
          { type: 'help_received', count: 12 }
        ],
        expectedOutcome: 'Membro respeitado da comunidade'
      }
    };

    const scenario = scenarios[scenarioName];
    if (!scenario) return null;

    // Simula as ações
    const userId = `sim_${Date.now()}`;
    scenario.actions.forEach(action => {
      for (let i = 0; i < action.count; i++) {
        this.interactions.push({
          userId,
          type: action.type,
          timestamp: new Date(),
          simulated: true
        });
      }
    });

    // Calcula resultado
    const reputation = this.calculateReputation(userId);
    const issues = this.identifyProblematicBehavior(userId);
    const response = this.applyCommunityResponse(userId, issues.overallSeverity);

    return {
      scenario: scenarioName,
      description: scenario.description,
      reputation,
      issues,
      communityResponse: response,
      expectedOutcome: scenario.expectedOutcome,
      actualOutcome: this.interpretOutcome(reputation, issues)
    };
  }

  interpretOutcome(reputation, issues) {
    if (reputation.status === 'exemplary') {
      return 'Usuário se torna líder natural da comunidade';
    }
    if (reputation.status === 'good') {
      return 'Usuário respeitado e bem integrado';
    }
    if (reputation.status === 'neutral') {
      return 'Usuário comum sem destaque especial';
    }
    if (issues.overallSeverity === 'high' || issues.overallSeverity === 'critical') {
      return 'Usuário gradualmente isolado pela comunidade';
    }
    return 'Usuário precisa melhorar comportamento';
  }
}

// 🧪 Exemplo de Uso
const community = new CommunityRegulation();

// Simula diferentes tipos de usuários
console.log('=== Simulação: Usuário Parasita ===');
const parasiticResult = community.simulateScenario('parasitic_user');
console.log(JSON.stringify(parasiticResult, null, 2));

console.log('\n=== Simulação: Contribuidor Generoso ===');
const generousResult = community.simulateScenario('generous_contributor');
console.log(JSON.stringify(generousResult, null, 2));

console.log('\n=== Simulação: Usuário Equilibrado ===');
const balancedResult = community.simulateScenario('balanced_user');
console.log(JSON.stringify(balancedResult, null, 2));

// Exemplo de como a comunidade responde naturalmente
console.log('\n=== Como a Comunidade Responde ===');
console.log('1. Usuário Parasita:', parasiticResult.communityResponse.actions);
console.log('2. Contribuidor Generoso:', community.recognizePositiveBehavior(generousResult.reputation.userId));
console.log('3. Usuário Equilibrado:', balancedResult.communityResponse.actions);

export { CommunityRegulation };