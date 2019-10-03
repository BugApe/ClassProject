<!--suppress HtmlUnknownAnchorTarget, CheckEmptyScriptTag -->
<template>
    <div id="home">
        <!-- 导航 -->
        <nav id="mainNav"
             class="navbar navbar-expand-lg navbar-light fixed-top py-3">
            <div class="container">
                <a href="#home" class="navbar-brand js-scroll-trigger">
                    <span class="navbar-brand-inverted-pink">I</span><span class="navbar-brand-inverted-blue">m</span><span class="navbar-brand-inverted-green">a</span><span class="navbar-brand-inverted-yellow">g</span><span class="navbar-brand-inverted-pink">e</span>2<span class="navbar-brand-inverted-blue">A</span><span class="navbar-brand-inverted-green">r</span><span class="navbar-brand-inverted-yellow">t</span>
                </a>
                <button class="navbar-toggler navbar-toggler-right" type="button" data-toggle="collapse"
                        data-target="#navbarResponsive" aria-controls="navbarResponsive" aria-expanded="false"
                        aria-label="Toggle navigation">
                    <span class="navbar-toggler-icon"></span>
                </button>
                <div class="collapse navbar-collapse" id="navbarResponsive">
                    <ul class="navbar-nav ml-auto my-2 my-lg-0">
                        <li class="nav-item">
                            <a href="#home" class="nav-link js-scroll-trigger">
                               首页
                            </a>
                        </li>
                        <li class="nav-item">
                            <a href="/Cartoon " class="nav-link js-scroll-trigger">头像转换</a>
                        </li>
                        <li class="nav-item">
                            <a href="/TransferStyle" class="nav-link js-scroll-trigger">风格融合</a>
                        </li>
                        <li class="nav-item">
                            <a href="/Doodle" class="nav-link js-scroll-trigger">艺术涂鸦</a>
                        </li>
                        <li class="nav-item">
                            <a href="/" class="nav-link js-scroll-trigger">美颜滤镜</a>
                        </li>
                        <li class="nav-item">
                            <a href="#about" class="nav-link js-scroll-trigger">
                               详情
                            </a>
                        </li>
                        <li class="nav-item">
                            <a href="#contact" class="nav-link js-scroll-trigger">
                              联系我们
                            </a>
                        </li>
                    </ul>
                </div>
            </div>
        </nav>
<header class="masthead_V">
            <div class="container h-100">
                <div class="row h-100 align-items-center justify-content-center">
                   <div class="container">
                <div class="row justify-content-center">
                    <div class="col-lg-12 text-center text-light py-5">
                       <br/><br/><br/><br/><br/><br/><br/><br/>
                        <a href="/Cartoon"
                           class="mt-5 btn btn-primary px-5 btn-xl js-scroll-trigger"
                           style="font-size: 2rem;background-color:#f06292">
                            头像转换
                        </a>&nbsp;&nbsp;
                        <a href="/TransferStyle"
                           class="mt-5 btn btn-primary px-5 btn-xl js-scroll-trigger"
                           style="font-size: 2rem;background-color:#3498DB ">
                            风格融合
                        </a>&nbsp;&nbsp;
                          <a href="/Doodle"
                           class="mt-5 btn btn-primary px-5 btn-xl js-scroll-trigger"
                           style="font-size: 2rem;background-color:#657350 ">
                            艺术涂鸦
                        </a>&nbsp;&nbsp;
                          <a href="/"
                           class="mt-5 btn btn-primary px-5 btn-xl js-scroll-trigger"
                           style="font-size: 2rem ;background-color:#a77f5c;color:#fff">
                            美颜滤镜
                        </a>
                    </div>
                </div>
                </div>
                </div>
            </div>
        </header>


        <!-- About 部分 -->
        <section id="about" class="page-section">
            <div class="container carousel-container text-center">
                <h2 class="mt-0">
                     <span class="text-primary font-weight-bold">Image</span>2<span class="text-primary font-weight-bold">Art</span>官方网站
                </h2>
                <div class="my-5 text-muted" style="line-height: 2em;font-size: 1.1em">
                   <p style="font-size: 1.3em">网站介绍</p>
                     <span class="text-primary font-weight-bold">头像转换</span>基于<a href="https://arxiv.org/abs/1907.10830">
                        生成对抗网络(GAN)
                    </a>实现<br>
                    <span class="text-primary font-weight-bold">艺术涂鸦</span>基于<a href="https://arxiv.org/abs/1603.01768">
                    Semantic Style Transfer
                </a>以及<a href="https://arxiv.org/abs/1601.04589">
                    Neural Patches
                </a>实现<br>
                    <span class="text-primary font-weight-bold">风格融合</span>基于<a href="https://arxiv.org/abs/1603.01768">
                    A Neural Algorithm of Artistic Style
                </a>实现<br>
                    <span class="text-primary font-weight-bold">人脸识别以及美颜</span>基于<a href="https://opencv.org/">
                    OpenCV
                </a>实现<br>
                    <span class="text-primary font-weight-bold">客户端渲染框架</span>使用<a href="https://cn.vuejs.org/">
                    Vue
                </a><br>
                    <span class="text-primary font-weight-bold">本网站</span>使用<a href="https://cn.vuejs.org/">
                    某某云
                </a>加速<br>
                </div>
                <div class="mt-5">
                    <div class="large-caption text-primary">
                        <div class="spinner-grow" style="width: 0.5em; height: 0.5em; margin-bottom: 0em;"></div>
                        {{ estimateCounter.toLocaleString() }}
                        <div class="spinner-grow" style="width: 0.5em; height: 0.5em; margin-bottom: 0em;"></div>
                    </div>
                    <div class="text-primary text-uppercase mt-4">selfies &amp; counting</div>
                </div>
            </div>
        </section>
        <!-- Contect部分 -->
        <section id="contact" class="page-section">
            <div class="container">
                <div class="row justify-content-center mb-5">
                    <div class="col-lg-8 text-center">
                        <h3 class="mt-0">Want to get in touch?</h3>
                        <hr class="divider my-5">
                        <p class="text-muted mb-4">
                            到GitHub上来下载我们的项目源码，关注项目的最新进展。如果您有任何问题和建议，请尽管对我们留言！
                        </p>
                    </div>
                </div>
                <div class="row text-center">
                    <div class="col-12 col-sm-6" style="margin: 0 auto">
                        <i style="color: #211f1f" class="fa fa-github fa-5x mb-3"></i>
                        <a class="d-block" href="https://github.com/BugApe" target="_blank">@BugApe</a>
                    </div>
                </div>
            </div>
        </section>
        <!-- Footer -->
        <footer class="bg-light py-5">
            <div class="container">
                <hr />
                <div class="small text-center text-muted">
                    Copyright &copy; 2019 by
                    <a href="https://github.com/BugApe">BugApe</a>&amp;<a href="https://github.com/longyunyun">longyunyun</a>
                    &amp;<a href="https://github.com/tcheng02">tcheng02</a>&amp;<a href="https://github.com/longyunyun">longyunyun</a>
                </div>
            </div>
        </footer>
    </div>
</template>

<!--suppress JSMethodCanBeStatic, JSUnusedGlobalSymbols, TypeScriptCheckImport -->
<script lang="ts">
    import {
        Component,
        Vue,
    } from "vue-property-decorator";

    import axios from "axios";
    import * as creative from "@/vendor/creative";
    export default class Home extends Vue {
        carouselImageCount = 22;
        counter = 0;
        estimateCounter = 0;
        counterTimestamp = 0;
        selfiesPerSecond = 0;
        counterIntervalHandle = 0;
        transparent1x1 = "data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7";
        onUpdateCounter() {
            this.estimateCounter = Math.ceil(
                this.counter
                + (Date.now() / 1000 - this.counterTimestamp)
                * this.selfiesPerSecond,
            );
        }
        async fetchStats() {
            // TODO: Replace current manually calculated estimates with actual real-time numbers once back-end is done.
            this.counter = 470444;
            this.selfiesPerSecond = 0.241254;
            this.counterTimestamp = 1567246919;
            this.estimateCounter = this.counter;
            if(this.counterIntervalHandle) {
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
            if(this.counterIntervalHandle) {
                clearInterval(this.counterIntervalHandle);
            }
        }
    }
</script>

<style lang="scss" scoped>
    section h2, .large-caption {
        font-size: 2.8em;
        line-height: 2.8;
        @media (max-width: 576px) {
            font-size: 2.0em;
        }
    }
    .nav-item, .page-section h2 {
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
        color: #f06292;
    }
     #mainNav .navbar-brand-inverted-pink {
        color: #f06292;
    }
     #mainNav .navbar-brand-inverted-blue {
        color: #3498DB;
    }
     #mainNav .navbar-brand-inverted-green {
        color: #657350;
    }
       #mainNav .navbar-brand-inverted-yellow {
        color: #a77f5c;
    }
    #mainNav {
        background: rgba(30, 30, 30, 0.8);
    }
    #mainNav.navbar-scrolled {
        background: #fff;
        .navbar-brand {
            color: #f06292;
        }
        .navbar-brand-inverted {
            color: #212529;
        }
    }
</style>
