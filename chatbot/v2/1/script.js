// script.js

const state = {
  isDark: false,
  messages: []
};

document.addEventListener('DOMContentLoaded', () => {
  lucide.createIcons();  // Initialize icons
  init();
});

function init() {
  renderMessages();
  loadSettings();
  setupEventListeners();
}

function toggleTheme() {
  document.body.classList.toggle('dark');
  state.isDark = !state.isDark;
  themeToggle.textContent = state.isDark ? '☀️' : '🌙';
}

function openSettings() {
  document.getElementById('settingsDialog').style.display = 'flex';
}

function closeSettings() {
  document.getElementById('settingsDialog').style.display = 'none';
}

function renderMessages() {
  const messagesContainer = document.getElementById('messagesContainer');
  messagesContainer.innerHTML =
      state.messages
          .map(
              message => `
        <div class="message ${message.role}">
            <div class="avatar">
                <i data-lucide="${
                  message.role === 'user' ? 'user' : 'bot'}"></i>
            </div>
            <div class="message-content">
                ${message.content || ''}
                ${message.status === 'typing' ? renderTypingIndicator() : ''}
                <div class="timestamp">${formatTime(message.timestamp)}</div>
                <div class="message-actions">
                    <button class="action-button" onclick="copyMessage('${
                  message.id}')">
                        <i data-lucide="copy"></i>
                    </button>
                    <button class="action-button" onclick="toggleSpeech('${
                  message.id}')">
                        <i data-lucide="volume-2"></i>
                    </button>
                    <button class="action-button" onclick="handleReaction('${
                  message.id}', 'thumbsUp')">
                        <i data-lucide="thumbs-up"></i>
                        <span>${message.reactions?.thumbsUp || 0}</span>
                    </button>
                    <button class="action-button" onclick="handleReaction('${
                  message.id}', 'thumbsDown')">
                        <i data-lucide="thumbs-down"></i>
                        <span>${message.reactions?.thumbsDown || 0}</span>
                    </button>
                </div>
            </div>
        </div>
    `).join('');

  lucide.createIcons();  // Reinitialize icons after rendering
  handleScroll();
}

function formatTime(timestamp) {
  const date = new Date(timestamp);
  return date.toLocaleTimeString([], {hour: '2-digit', minute: '2-digit'});
}

function renderTypingIndicator() {
  return `<span class="typing">...</span>`;
}

function sendMessage() {
  const inputField = document.getElementById('inputField');
  const content = inputField.value.trim();
  if (!content) return;

  const userMessage = {
    id: `msg-${Date.now()}`,
    role: 'user',
    content,
    timestamp: Date.now(),
    reactions: {thumbsUp: 0, thumbsDown: 0}
  };

  state.messages.push(userMessage);
  inputField.value = '';
  renderMessages();
  simulateResponse(userMessage.id);
}

function simulateResponse(userMessageId) {
  const assistantMessage = {
    id: `msg-${Date.now() + 1}`,
    role: 'assistant',
    content: 'Typing...',
    status: 'typing',
    timestamp: Date.now(),
    reactions: {thumbsUp: 0, thumbsDown: 0}
  };

  state.messages.push(assistantMessage);
  renderMessages();

  setTimeout(() => {
    assistantMessage.content = 'I\'m here to help!';
    assistantMessage.status = 'sent';
    renderMessages();
  }, 1000);
}

function setupEventListeners() {
  document.getElementById('sendButton').addEventListener('click', sendMessage);
  document.getElementById('inputField').addEventListener('keydown', (event) => {
    if (event.key === 'Enter') sendMessage();
  });
}

function handleScroll() {
  const messagesContainer = document.getElementById('messagesContainer');
  messagesContainer.scrollTop = messagesContainer.scrollHeight;
}

function copyMessage(id) {
  const message = state.messages.find(msg => msg.id === id);
  if (message) {
    navigator.clipboard.writeText(message.content)
        .then(() => alert('Message copied to clipboard!'))
        .catch(() => alert('Failed to copy message.'));
  }
}

function toggleSpeech(id) {
  const message = state.messages.find(msg => msg.id === id);
  if (message && 'speechSynthesis' in window) {
    const utterance = new SpeechSynthesisUtterance(message.content);
    speechSynthesis.speak(utterance);
  }
}

function handleReaction(id, type) {
  const message = state.messages.find(msg => msg.id === id);
  if (message && message.reactions) {
    message.reactions[type]++;
    renderMessages();
  }
}
