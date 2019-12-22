<template>
  <div id="transferStyle">
    <!-- 导航 -->
    <nav id="mainNav" class="navbar navbar-expand-lg navbar-light fixed-top py-4">
      <div class="container">
        <a href="#doodle" class="navbar-brand js-scroll-trigger" style="position: absolute;left: 6%">
          <span class="navbar-brand-inverted">Image</span>2<span class="navbar-brand-inverted">Art | </span><span
            class="small text-center navbar-brand-inverted">照片风格化</span>
        </a>
        <button class="navbar-toggler navbar-toggler-right" type="button" data-toggle="collapse"
          data-target="#navbarResponsive" aria-controls="navbarResponsive" aria-expanded="false"
          aria-label="Toggle navigation">
          <span class="navbar-toggler-icon"></span>
        </button>
        <div class="collapse navbar-collapse" id="navbarResponsive">
          <ul class="navbar-nav ml-auto my-2 my-lg-0" style="position: absolute;right:6%">
            <li class="nav-item">
              <router-link to="/" class="nav-link js-scroll-trigger">
                首页
              </router-link>
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
          </ul>
        </div>
      </div>
    </nav>

    <!-- 头部 -->
    <header class="masthead">
      <div class="container h-100">
        <div class="row h-100 align-items-center justify-content-center">
          <div class="col-lg-10 align-self-center">
            <PhotoUploader>
            </PhotoUploader>
          </div>
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
  import * as creative from "@/vendor/creative";
  import photoUploader from "@/components/StyleUploader.vue";

  @Component({
    components: {
      PhotoUploader: photoUploader
    }
  })
  export default class TransferStyle extends Vue {
    carouselImageCount = 22;
    counter = 0;
    estimateCounter = 0;
    counterTimestamp = 0;
    selfiesPerSecond = 0;
    counterIntervalHandle = 0;
    transparent1x1 =
      "data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7";
    onUpdateCounter() {
      this.estimateCounter = Math.ceil(
        this.counter +
          (Date.now() / 1000 - this.counterTimestamp) * this.selfiesPerSecond
      );
    }

    async fetchStats() {
      // TODO: Replace current manually calculated estimates with actual real-time numbers once back-end is done.
      this.counter = 470444;
      this.selfiesPerSecond = 0.241254;
      this.counterTimestamp = 1567246919;
      this.estimateCounter = this.counter;

      if (this.counterIntervalHandle) {
        clearInterval(this.counterIntervalHandle);
      }

      this.onUpdateCounter();
      this.counterIntervalHandle = window.setInterval(this.onUpdateCounter, 4000);

      // try {
      //     const response = await axios.get(process.env.VUE_APP_API_COUNT_URL);
      //     this.counter = parseInt(response.data["count"]);
      //     this.selfiesPerSecond = parseFloat(response.data["sps"]);
      //     this.counterTimestamp = Date.now();
      //     this.estimateCounter = this.counter;
      //
      //     if(this.counterIntervalHandle) {
      //         clearInterval(this.counterIntervalHandle);
      //     }
      //
      //     this.onUpdateCounter();
      //     this.counterIntervalHandle = setInterval(this.onUpdateCounter, 4000);
      // } catch(e) {
      //     // tslint:disable-next-line
      //     console.log(e);
      // }
    }

    mounted() {
      this.fetchStats();
      creative.init(jQuery);
    }

    beforeDestroy() {
      if (this.counterIntervalHandle) {
        clearInterval(this.counterIntervalHandle);
      }
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

header.masthead {
  background: -webkit-gradient(
      linear,
      left top,
      left bottom,
      from(rgba(16, 30, 68, 0.6)),
      to(rgba(27, 41, 63, 0.4))
    ),
    url("../../public/img/bg-masthead_D.jpg");
  background: linear-gradient(
      to bottom,
      rgba(16, 30, 68, 0.6) 0,
      rgba(27, 36, 67, 0.4) 100%
    ),
    url("../../public/img/bg-masthead_D.jpg");
}

.nav-item,
.page-section h2 {
  text-transform: uppercase;
}

.nav-item .nav-link {
  font-size: 1.2rem !important;
}

#mainNav .navbar-brand {
  font-size: 1.7rem !important;
  color: rgba(255, 255, 255, 0.7);
}

#mainNav .navbar-brand-inverted {
  color: #3498db;
}

#mainNav {
  background: rgba(30, 30, 30, 0.8);
}

#mainNav.navbar-scrolled {
  background: #fff;

  .navbar-brand {
    color: #3498db;
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

.text-primary {
  color: #3498db !important;
}
</style>
