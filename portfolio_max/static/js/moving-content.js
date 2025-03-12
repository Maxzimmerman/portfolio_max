const TodoAppLink = document.querySelector('.project-git-link-todoapp');
const WebDirectory = document.querySelector('.project-git-link-webdirectory');
const Elbigote = document.querySelector('.project-git-link-elbigote');

TodoAppLink.addEventListener('click', () => {
   window.location='https://www.example.com';
});

WebDirectory.addEventListener('click', () => {
   window.location.href = "https://brittanychiang.com/"
});

Elbigote.addEventListener('click', () => {
   window.location.href = "https://github.com/Maxzimmerman/ElBigote"
});