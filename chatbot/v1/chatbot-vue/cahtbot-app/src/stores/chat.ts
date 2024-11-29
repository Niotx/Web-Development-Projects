// src/stores/chat.ts
import type {Language, Message, Translation} from '@/types'
import {defineStore} from 'pinia'

export const useChatStore = defineStore('chat', {
  state: () => ({
    isDark: false,
    currentLang: 'fa' as keyof typeof languages,
    messages: [] as Message[],
    isTyping: false,
    isRecording: false,

    languages: {
      fa: {name: 'فارسی', dir: 'rtl'},
      en: {name: 'English', dir: 'ltr'},
      ar: {name: 'العربية', dir: 'rtl'},
      tr: {name: 'Türkçe', dir: 'ltr'},
      fr: {name: 'Français', dir: 'ltr'}
    } as Record<string, Language>,

    translations: {
      fa: {
        chatHistory: 'تاریخچه گفتگو',
        typeMessage: 'پیام خود را بنویسید...',
        suggestions: [
          'چطور می‌توانم کمک کنم؟', 'سوالات متداول',
          'راهنمایی بیشتر'
        ]
      },
      en: {
        chatHistory: 'Chat History',
        typeMessage: 'Type your message...',
        suggestions: ['How can I help?', 'FAQ', 'More guidance']
      },
      ar: {
        chatHistory: 'سجل المحادثة',
        typeMessage: 'اكتب رسالتك...',
        suggestions:
            ['كيف يمكنني المساعدة؟', 'الأسئلة الشائعة', 'المزيد من التوجيه']
      },
      tr: {
        chatHistory: 'Sohbet Geçmişi',
        typeMessage: 'Mesajınızı yazın...',
        suggestions:
            ['Nasıl yardımcı olabilirim?', 'SSS', 'Daha fazla rehberlik']
      },
      fr: {
        chatHistory: 'Historique',
        typeMessage: 'Écrivez votre message...',
        suggestions: ['Comment puis-je aider?', 'FAQ', 'Plus de conseils']
      }
    } as Record<string, Translation>
  }),

  actions: {
    toggleDarkMode() {
      this.isDark = !this.isDark
    },

    setLanguage(lang: string) {
      if (lang in this.languages) {
        this.currentLang = lang as keyof typeof languages
      }
    },

    async sendMessage(message: string) {
      if (!message.trim())
        return

            // Add user message
            this.messages
                .push({
                  id: this.messages.length + 1,
                  message,
                  isBot: false,
                  timestamp: new Date()
                })

            // Show typing indicator
            this.isTyping =
                true

                // Simulate bot response
                await new Promise(resolve => setTimeout(resolve, 1500))

                // Add bot response
                this.messages
                    .push({
                      id: this.messages.length + 1,
                      message: this.translations[this.currentLang]
                                   .suggestions[Math.floor(Math.random() * 3)],
                      isBot: true,
                      timestamp: new Date()
                    })

                        this.isTyping = false
    },

    async handleFile(file: File) {
      this.messages.push({
        id: this.messages.length + 1,
        message: `File: ${file.name}`,
        isBot: false,
        timestamp: new Date(),
        isFile: true
      })
    },

    toggleRecording() {
      this.isRecording = !this.isRecording
    }
  }
})
