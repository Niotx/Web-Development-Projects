// src/types/index.ts
export interface Message {
  id: number
  message: string
  isBot: boolean
  timestamp: Date
  isFile?: boolean
}

export interface Language {
  name: string
  dir: 'rtl'|'ltr'
}

export interface Translation {
  chatHistory: string
  typeMessage: string
  suggestions: string[]
}