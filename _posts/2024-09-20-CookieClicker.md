---
layout: base
title: Cookie Clicker
---
<!-- Cookie Clicker Game html -->

<div style="text-align: center; margin-top: 50px;">
    <!-- Cookie Image -->
    <img id="cookie" src="{{site.baseurl}}/images/cookie.webp" alt="Cookie" style="width: 170px; height: 170px; cursor: pointer;">
    <!-- Display Score -->
    <div id="score" style="font-size: 24px; margin-top: 20px;">Cookies: 0</div>
    <!-- Shop -->
  
</div>
<!-- Audio for Cookie Eating Noise-->
<audio id="clickSound" src="{{site.baseurl}}/audios/easportssound.mp3">


<!-- Cookie Clicker Game -->
<script>
    //define variables
    let score = 0;
    const clickSound = document.getElementById('clickSound');

    //Click the Cookie to gain one
    document.getElementById('cookie').addEventListener('click', function() {
        score+=1;
        document.getElementById('score').textContent = 'Cookies: ' + score;

        //play the cookie eating noise
        clickSound.play()
    });
</script>