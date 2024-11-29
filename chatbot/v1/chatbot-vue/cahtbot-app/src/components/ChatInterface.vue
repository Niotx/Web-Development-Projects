<!-- src/components/ChatInterface.vue -->
<template>
  <div class="vh-100" :class="{ 'dark-mode': store.isDark }">
    <div class="container-fluid h-100">
      <div class="row h-100">
        <!-- Sidebar -->
        <div
          class="col-md-3 col-lg-3 p-3 sidebar"
          :class="store.languages[store.currentLang].dir"
        >
          <div class="d-flex justify-content-between align-items-center mb-4">
            <h4 class="mb-0">
              {{ store.translations[store.currentLang].chatHistory }}
            </h4>
            <i class="fas fa-comments"></i>
          </div>

          <div class="chat-history">
            <div
              v-for="chat in store.messages"
              :key="chat.id"
              class="p-3 rounded hover-scale mb-2 chat-history-item"
            >
              <div>{{ chat.message }}</div>
              <small class="text-muted">{{
                chat.timestamp.toLocaleTimeString()
              }}</small>
            </div>
          </div>
        </div>

        <!-- Main Chat Area -->
        <div class="col-md-9 col-lg-9 p-0 d-flex flex-column">
          <!-- Header -->
          <ChatHeader />

          <!-- Messages Area -->
          <div class="chat-container p-3" ref="chatContainer">
            <div v-for="msg in store.messages" :key="msg.id">
              <div :class="[msg.isBot ? 'message-bot' : 'message-user']">
                {{ msg.message }}
              </div>
            </div>
            <div v-if="store.isTyping" class="message-bot typing-indicator">
              typing...
            </div>
          </div>

          <!-- Input Area -->
          <ChatInput @send="handleSend" />
        </div>
      </div>
    </div>
  </div>
</template>

<script setup lang="ts">
import { ref, onMounted, nextTick } from 'vue'
import { useChatStore } from '@/stores/chat'
import ChatHeader from './ChatHeader.vue'
import ChatInput from './ChatInput.vue'

const store = useChatStore()
const chatContainer = ref<HTMLElement | null>(null)

const scrollToBottom = async () => {
  await nextTick()
  if (chatContainer.value) {
    chatContainer.value.scrollTop = chatContainer.value.scrollHeight
  }
}

const handleSend = async (message: string) => {
  await store.sendMessage(message)
  scrollToBottom()
}

onMounted(() => {
  scrollToBottom()
})
</script>

<style lang="scss">
@import '@/assets/styles/variables';
@import 'bootstrap/scss/bootstrap';
@import '@fortawesome/fontawesome-free/css/all.css';
@import url('https://fonts.googleapis.com/css2?family=Vazirmatn:wght@400;700&display=swap');

.dark-mode {
  --primary-gradient: linear-gradient(135deg, #1a472a 0%, #2d5a40 100%);
  --secondary-gradient: linear-gradient(135deg, #2d5a40 0%, #1a472a 100%);
  background-color: #1a1a1a;
  color: white;
}

.sidebar {
  background: var(--secondary-gradient);
  transition: all 0.3s ease;
}

.chat-container {
  height: calc(100vh - 140px);
  overflow-y: auto;
}

.message-bot,
.message-user {
  border-radius: 15px;
  padding: 10px 15px;
  margin: 5px 0;
  max-width: 80%;
  animation: fadeIn 0.3s ease-in-out;
}

.message-bot {
  background: rgba(0, 0, 0, 0.05);
}

.message-user {
  background: var(--primary-gradient);
  color: white;
  margin-left: auto;
}

.rtl {
  direction: rtl;
  font-family: 'Vazirmatn', sans-serif;
}

.ltr {
  direction: ltr;
}

@keyframes fadeIn {
  from {
    opacity: 0;
    transform: translateY(10px);
  }
  to {
    opacity: 1;
    transform: translateY(0);
  }
}

.typing-indicator {
  animation: pulse 1s infinite;
}

@keyframes pulse {
  0% {
    opacity: 0.5;
  }
  50% {
    opacity: 1;
  }
  100% {
    opacity: 0.5;
  }
}
</style>