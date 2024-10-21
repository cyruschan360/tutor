(function() {
  // Load zh-tw | zh-cn translation
  const courseCode = location.href.match(/JCECC\+[BMA][0-9]{2}([TS])\+[0-9]+/);
  const lang = courseCode ? courseCode[1] : false;
  const langCode = (lang === 'S') ? 'zh-cn' : 'zh-tw';
  const cookie = document.cookie.match(/openedx-language-preference=(en|zh-cn|zh-tw)/);
  const cookieLangCode = cookie ? cookie[1] : false;
  if (lang && cookieLangCode && (cookieLangCode !== langCode)) {
    document.cookie = `openedx-language-preference=${langCode}; Domain=.jcecc.hk; Path=/`;
    location.reload();
  }

  // Redirect openedx home to project website
  const isHome = location.href.match(/^https\:\/\/learn-v2\.jcecc\.hk\/?$/);
  const langParam = (langCode === 'zh-cn') ? 'zh_CN' : 'zh_TW';
  const permalink = (langCode === 'zh-cn') ? '%E4%B8%BB%E9%A1%B5/' : '';
  const homeUrl =  `https://learn-v2.jcecc.hk/portal/${permalink}`;
  if (isHome) {
    location.replace(homeUrl);
  }

  // Translate login page
  const isCasLogin = location.href.match(/^https\:\/\/learn-v2\.jcecc\.hk\/cas\/login\/?/);
  if (isCasLogin) {
    const username = (cookieLangCode === 'zh-cn') ? '帐号' : '帳號';
    const usernameLabel = document.querySelector('label[for="id_username"]');
    const usernameInput = document.getElementById('id_username');
    if (usernameLabel && usernameInput) {
      usernameLabel.innerHTML = username;
      usernameInput.setAttribute('placeholder', username);
    }
    
    const password = (cookieLangCode === 'zh-cn') ? '密码' : '密碼';
    const passwordLabel = document.querySelector('label[for="id_password"]');
    const passwordInput = document.getElementById('id_password');
    if (passwordLabel && passwordInput) {
      passwordLabel.innerHTML = password;
      passwordInput.setAttribute('placeholder', password);
    }

    const login = (cookieLangCode === 'zh-cn') ? '登入' : '登入';
    const loginBtn = document.querySelector('button[type="submit"]');
    if (loginBtn) {
      loginBtn.innerHTML = login;
    }    
  }

  // Redirect to JCECC website for registration
  let redirectTimer = setInterval( () => {    
    const isAnonymous = document.querySelector('a[href*="/register"],#register-user');
    const isLoginPage = location.href.match(/\/authn\/login/);
    const isCASPage = location.href.match(/\/auth\/cas\/login/);
    if ((isAnonymous || isLoginPage) && !isCASPage) {
        location.assign('https://learn-v2.jcecc.hk/auth/cas/login');
        clearInterval(redirectTimer);
    }
  }, 500);

  // Replace login links
  let loginTimer = setInterval( () => {
    const loginLinks = document.querySelectorAll('a[href*="/login"]');
    loginLinks.forEach( el => {
        let href = el.getAttribute('href').replace(/\/\/learn-v2\.jcecc\.hk\/login/, "//learn-v2.jcecc.hk/auth/cas/login");
        el.setAttribute('href', href);
    });
  }, 1000);
   
  // Add frontend link in top menu
  const homeLabel = (cookieLangCode === 'zh-cn') ? '主页' : '主頁';
  const dashboardLabel = (cookieLangCode === 'zh-cn') ? '返回课程目录' : '返回課程目錄';

  let topMenuTimer = setInterval( () => {
    let topMenu = document.querySelector('.global-header .main');
    let topLink = document.createElement("div");
    let isLoaded = document.querySelector('.jcecc.topLink');
    if (topMenu && !isLoaded) {
        topLink.classList.add('mobile-nav-item', 'hidden-mobile', 'nav-item', 'nav-tab', 'jcecc', 'topLink');
        topLink.innerHTML = `<a class="tab-nav-link" href="${homeUrl}" aria-current="page">${homeLabel}</a>`;
        topMenu.prepend(topLink);
    }
  }, 1000);
  
  let topAppMenuTimer = setInterval( () => {
    let topAppMenu = document.querySelector('#courseTabsNavigation nav');
    let topAppLink = document.createElement("a");
    let isLoaded = document.querySelector('.jcecc.topAppLink');
    if (topAppMenu && !isLoaded) {
        topAppLink.classList.add('nav-item', 'flex-shrink-0', 'nav-link', 'jcecc', 'topAppLink');
        topAppLink.setAttribute('href', homeUrl);
        topAppLink.innerHTML = homeLabel;
        topAppMenu.prepend(topAppLink);
    }
  }, 1000);

  // Add frontend link in drop-down menu
  let dropdownMenuTimer = setInterval( () => {
    let dropdownMenu = document.getElementById('user-menu');
    let dropdownLink = document.createElement("div");
    let dashboardLink = document.createElement("div");
    let isLoaded = document.querySelector('.jcecc.dropdownLink');
    if (dropdownMenu && !isLoaded) {
        dropdownLink.classList.add('mobile-nav-item', 'dropdown-item', 'dropdown-nav-item', 'jcecc', 'dropdownLink');
        dropdownLink.innerHTML = `<a href="${homeUrl}" role="menuitem">${homeLabel}</a>`;
        dropdownMenu.prepend(dropdownLink);

        dashboardLink.classList.add('mobile-nav-item', 'dropdown-item', 'dropdown-nav-item', 'jcecc', 'dashboardLink');
        dashboardLink.innerHTML = `<a href="//learn-v2.jcecc.hk/dashboard" role="menuitem">${dashboardLabel}</a>`;
        dropdownMenu.prepend(dashboardLink);
    }
  }, 1000);

  // Translate logout button
  let dropdownAppMenuTimer = setInterval( () => {
    let dropdownAppMenuBtn = document.querySelector('.learning-header .user-dropdown button');
    let isLoaded = dropdownAppMenuBtn && dropdownAppMenuBtn.classList.contains("dropdownAppMenuBtn");
    if (dropdownAppMenuBtn && !isLoaded) {
      dropdownAppMenuBtn.classList.add('jcecc', 'dropdownAppMenuBtn');
      dropdownAppMenuBtn.addEventListener("click", (e) => {
          setTimeout( () => {
              let logoutBtn = document.querySelector('.learning-header .user-dropdown a[href*="/logout"]');
              if (logoutBtn) {
                  logoutBtn.innerHTML = (cookieLangCode === 'zh-cn') ? '登出' : '登出';
              }

              let dropdownAppMenu = document.querySelector('.learning-header .user-dropdown > div');
              let isLinkExist = document.querySelector('.learning-header .user-dropdown a.frontend-home');
              let dropdownAppLink = document.createElement("a");
              let dashboardAppLink = document.createElement("a");
              if (dropdownAppMenu && !isLinkExist) {
                  dropdownAppLink.classList.add('pgn__dropdown-item', 'dropdown-item', 'frontend-home', 'jcecc', 'dropdownAppLink');
                  dropdownAppLink.setAttribute('href', link);
                  dropdownAppLink.innerHTML = homeLabel;
                  dropdownAppMenu.prepend(dropdownAppLink);

                  dashboardAppLink.classList.add('pgn__dropdown-item', 'dropdown-item', 'frontend-home', 'jcecc', 'dashboardAppLink');
                  dashboardAppLink.setAttribute('href', '//learn-v2.jcecc.hk/dashboard');
                  dashboardAppLink.innerHTML = dashboardLabel;
                  dropdownAppMenu.prepend(dashboardAppLink);
              }              
          }, 100);            
      });
    }
  }, 1000);

  // Modify notification message for ungraded quiz
  let timeout = setTimeout(function() {
      const header = document.getElementsByTagName('h1')[0].innerText;
      const isQuiz = header.match(/知識測驗/) || header.match(/知识测验/);
      
      let notificationMsg = document.querySelectorAll('.notification-message');
      notificationMsg.forEach(function(el){
          const matched = el.innerText.match(/Your answers were previously saved./);
          if (!isQuiz && matched) {
              el.innerText = 'Your answers were previously saved. Submission is not required for this question.';
          }
      });

      const saveBtn = document.querySelectorAll('button.save');
      saveBtn.forEach(function(el){
          el.style.display = 'none';
      });
  }, 1000);
  
})();

