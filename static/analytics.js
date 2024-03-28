function runAnalytics() {
    const script = document.createElement('script');
    script.async = true;
    script.defer = true;
    script.src = 'https://www.googletagmanager.com/gtag/js?id=G-X2WVN4SRD4';

    document.head.appendChild(script);
    window.dataLayer = window.dataLayer || [];
    function gtag() { dataLayer.push(arguments); }
    gtag('js', new Date());

    gtag('config', 'G-X2WVN4SRD4');
}

runAnalytics();