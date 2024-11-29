const vm = Vue.createApp({
                data() {
                  return {
                    firstName: 'Matin', lastName: 'Naseri',
                        url: 'https://google.com',
                        raw_url:
                      '<a href="https://google.com" target="_blank">Google</a>',
                        age: 20
                  }
                },
                methods: {
                  fullName() {
                    return this.firstName +' '+ this.lastName
                  },
                  increment() {
                    this.age++
                  },
                  updateLastName(event) {
                    this.lastName = event.target.value
                  }

                }
              })
               .mount('#app1')

           // setTimeout(() => {
           //     vm.firstName = 'Mohammad';
           // }, 2000);

           // Vue.createApp({
           //      data() {
           //        return {
           //          firstName: 'Matin', lastName: 'Naseri'
           //        }
           //      }
           //    }).mount('#app2')