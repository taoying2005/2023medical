// 页面加载完成后执行
window.addEventListener('DOMContentLoaded', function() {
    // 获取所有按钮
    const buttons = document.querySelectorAll('button[data-page]');
    
    // 为每个按钮添加点击事件
    buttons.forEach(button => {
        button.addEventListener('click', function() {
            // 获取目标页面ID
            const targetPageId = this.getAttribute('data-page');
            
            // 隐藏所有页面
            const allPages = document.querySelectorAll('div[id^="page"]');
            allPages.forEach(page => {
                page.style.display = 'none';
            });
            
            // 显示目标页面
            const targetPage = document.getElementById(targetPageId);
            if (targetPage) {
                targetPage.style.display = 'block';
            }
        });
    });
});