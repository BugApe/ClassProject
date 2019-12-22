<template>
  <div id="avatar">
    <!-- 导航 -->
    <nav id="mainNav" class="navbar navbar-expand-lg navbar-light fixed-top py-3">
      <div class="container">
        <a href="#avatar" class="navbar-brand js-scroll-trigger">
          <span class="navbar-brand-inverted">Image</span>2<span class="navbar-brand-inverted">Art</span>
        </a>
        <button class="navbar-toggler navbar-toggler-right" type="button" data-toggle="collapse"
          data-target="#navbarResponsive" aria-controls="navbarResponsive" aria-expanded="false"
          aria-label="Toggle navigation">
          <span class="navbar-toggler-icon"></span>
        </button>
        <div class="collapse navbar-collapse" id="navbarResponsive">
          <ul class="navbar-nav ml-auto my-2 my-lg-0">
            <li class="nav-item">
              <a href="/" class="nav-link js-scroll-trigger">
                首页
              </a>
            </li>
            <li class="nav-item">
              <router-link to="/Cartoon" class="nav-link js-scroll-trigger">头像转换</router-link>
            </li>
            <li class="nav-item">
              <router-link to="/TransferStyle" class="nav-link js-scroll-trigger">风格融合</router-link>
            </li>
            <li class="nav-item">
              <router-link to="/Doodle" class="nav-link js-scroll-trigger">艺术涂鸦</router-link>
            </li>
            <li class="nav-item">
              <router-link to="/Beauty" class="nav-link js-scroll-trigger">美颜滤镜</router-link>
            </li>
            <li class="nav-item">
              <router-link to="/#about" class="nav-link js-scroll-trigger">
                详情
              </router-link>
            </li>
            <li class="nav-item">
              <router-link to="/#contact" class="nav-link js-scroll-trigger">
                联系我们
              </router-link>
            </li>
          </ul>
        </div>
      </div>
    </nav>

    <!-- 头部 -->
    <!-- <header class="masthead">
      <div class="container h-100">
        <div class="row h-100 align-items-center justify-content-center">
          <div class="col-lg-10 align-self-center"> -->
 <!-- <a href="beauty.html"  class="nav-link js-scroll-trigger">美颜滤镜</a> -->
 <!-- <button type="button"  >美颜滤镜</button>
          </div>
        </div>
      </div>
    </header> -->
 <header class="masthead">
    
          <div class="container">
            
              <div class="col-lg-8 text-center text-light" style="position:absolute;bottom:20%">
                <button class="mt-5 btn btn-primary px-5 btn-xl js-scroll-trigger" @click="beauty()"
                  style="font-size: 2rem;background-color:#a77f5c">
                  风格滤镜
                </button>&nbsp;
                <button class="mt-5 btn btn-primary px-5 btn-xl js-scroll-trigger" @click="beauty()"
                  style="font-size: 2rem;background-color:#a77f5c">
                  亮度调节
                </button>&nbsp;
                <button class="mt-5 btn btn-primary px-5 btn-xl js-scroll-trigger" @click="beauty()"
                  style="font-size: 2rem;background-color:#a77f5c">
                  磨皮美白
                </button>&nbsp;
                <button class="mt-5 btn btn-primary px-5 btn-xl js-scroll-trigger"  @click="beauty()"
                  style="font-size: 2rem ;background-color:#a77f5c;color:#fff">
                  人脸识别
                </button>
            
            </div>
        
      </div>
    </header>
    <!-- Footer -->
    <footer class="bg-light py-5">
      <div class="container">
        <hr />
        <div class="small text-center text-muted">
          Copyright &copy; 2019 by
          <a href="https://github.com/BugApe">BugApe</a>&amp;<a href="https://github.com/longyunyun">longyunyun</a>
          &amp;<a href="https://github.com/tcheng02">tcheng02</a>&amp;<a
            href="https://github.com/zxw110111">zxw110111</a>
        </div>
      </div>
    </footer>
  </div>
</template>

<!--suppress JSMethodCanBeStatic, JSUnusedGlobalSymbols, TypeScriptCheckImport -->
<script lang="ts">

import { Component, Vue } from "vue-property-decorator";

import axios from "axios";

export default class Beauty extends Vue {

  mounted() {
   
  }
beauty(){
    var ws = new ActiveXObject("WScript.Shell");      
     ws.run('python E://BeautyCamera20190921/BeautyCamera20190921/BeautyCamera-master/main.py');
}

}
</script>

<style lang="scss" scoped>
$carousel-size: 100px;

section h2,
.large-caption {
  font-size: 2.8em;
  line-height: 1.25;

  @media (max-width: 576px) {
    font-size: 2em;
  }
}

.nav-item,
.page-section h2 {
  text-transform: uppercase;
}

.nav-item .nav-link {
  font-size: 1.2rem !important;
}

header.masthead {
  background: -webkit-gradient(
      linear,
      left top,
      left bottom,
      from(rgba(167,127,92, 0.6)),
      to(rgba(175, 140, 110, 0.4))
    ),
    url("../../public/img/bg-masthead_Do.jpg");
  background: linear-gradient(
      to bottom,
      rgba(167,127,92, 0.6) 0,
      rgba(179, 147, 119, 0.4) 100%
    ),
    url("../../public/img/bg-masthead_Do.jpg");
}
#mainNav .navbar-brand {
  font-size: 1.7rem !important;
  color: rgba(255, 255, 255, 0.7);
}

#mainNav .navbar-brand-inverted {
  color: #a77f5c;
}

#mainNav {
  background: rgba(30, 30, 30, 0.8);
}

#mainNav.navbar-scrolled {
  background: #fff;

  .navbar-brand {
    color: #a77f5c;
  }

  .navbar-brand-inverted {
    color: #212529;
  }
}

#portfolio .container-fluid {
  max-width: 12 * 160px;
}

.portfolio-box-caption {
  -webkit-transition: opacity 0.75s ease !important;
  transition: opacity 0.75s ease !important;
}
</style>
