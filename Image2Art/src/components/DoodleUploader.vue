<!--suppress HtmlFormInputWithoutLabel, HtmlUnknownTag -->
<template>
    <div ref="photo-uploader"
         class="photo-uploader shadow-sm">
        <div class="row">
             <div class="left">
                 <div class="row pre-scrollable">
                    <img v-image-preview ="{src:'/img/doodle/Gogh_sem.png' }" src="img/doodle/Gogh.jpg"  class="img-thumbnail" alt="Cinque Terre">
                    <img src="img/doodle/Renoir.jpg" v-image-preview ="{src:'/img/doodle/Renoir_sem.png' }" class="img-thumbnail" alt="Cinque Terre">
                    <img src="img/doodle/Mia.jpg" v-image-preview ="{src:'/img/doodle/Mia_sem.png' }" class="img-thumbnail" alt="Cinque Terre">
                    <img src="img/doodle/Freddie.jpg" v-image-preview ="{src:'/img/doodle/Freddie_sem.png' }" class="img-thumbnail" alt="Cinque Terre">
                    <img src="img/doodle/Monet.jpg" v-image-preview ="{src:'/img/doodle/Monet_sem.png' }" class="img-thumbnail" alt="Cinque Terre">
                    <img src="img/doodle/Seth.jpg" v-image-preview ="{src:'/img/doodle/Seth_sem.png' }" class="img-thumbnail" alt="Cinque Terre">
            </div>
            </div>
            <div  class="tab-content right">
            <div v-show="step === 'drop'"
                 class="drop-container col-sm">
                <div class="drop-container-inner">
                    <input id="photo-input"
                           type="file"
                           accept="image/*"
                           class="photo-input"
                           @change="onPhotoSelected" />
                    <label for="photo-input">
                         <h1 class="d-block text-uppercase mx-3 px-2 mx-lg-5 px-lg-4">
                            What do <span class="text-primary font-weight-bold">YOU</span>
                            look like in <span class="text-primary font-weight-bold">anime</span>?
                        </h1>
                        <i class="fa fa-cloud-upload fa-5x mt-4 mb-2 text-primary"></i>
                        <span class="d-block mb-4 text-primary">
                    上传涂鸦
                        </span>

                        <!--
                        <div role="alert"
                             class="alert alert-info mt-3 mx-5 small"
                             style="font-size: 11pt">
                            <strong>Heads up!</strong> Due to extremely high demand, we are
                            currently unable to send e-mails. ಥ_ಥ You can still upload your selfie now and
                            it'll be processed as soon as possible.
                        </div>
                        -->

                        <span class="text-muted"
                             style="font-size: 11pt;">
                            (您的隐私将会得到 <strong>绝对保护</strong>)
                        </span>
                    </label>
                </div>
            </div>
            <div v-show="step === 'crop'" class="crop-container col-sm">
                <div class="crop-container-inner text-center">
                      <div class="mt-5 mb-5" style="font-size: 1.2em">
                        Now please <span class="text-primary font-weight-bold">crop</span>
                        the photo to your <span class="text-primary font-weight-bold">face</span> only!
                    </div>
                    <Cropper ref="cropper"
                             class="mb-3"
                             :photoUrl="photoDataUrl" />
                    <button type="button"
                            class="btn btn-primary btn-lg p-3 mb-4 text-uppercase"

                            @click="onPhotoCropped">
                              Turn me into anime!
                    </button>
                </div>
            </div>
            <div v-show="step === 'email'"
                 class="email-container col-sm">
                <div class="mx-3 my-5">
                    <form class="my-md-5 py-md-4"
                          @submit.prevent="onUploadPhoto">
                        <div class="form-row mb-4 align-items-center justify-content-center">
                            <div class="col col-10 text-center">
                                 <div style="font-size: 1.2em; line-height: 1.8em">
                                    This is going to take a while!
                                    <span class="text-primary text-nowrap font-weight-bold">(◠‿◠)</span>
                                    We'll send <span class="text-primary font-weight-bold">your anime selfie</span>
                                    to <span class="text-primary font-weight-bold">your email</span> once it's ready.  </div>
                            </div>
                        </div>
                        <div class="form-row justify-content-center text-center">
                            <div class="col-12 mb-2 col-md-8">
                                <input required
                                       type="email"
                                       class="form-control form-control-lg"
                                         placeholder="Enter your e-mail address…"

                                       v-model="email" />
                            </div>
                            <div class="col-12 col-md-2">
                                <button type="submit"
                                        :class="['btn btn-primary btn-lg btn-block text-uppercase',
                                                 canSubmit ? '' : 'disabled']">
                                 Upload
                                </button>
                            </div>

                            <div class="col-12 mt-2 col-md-10 mt-md-0">
                                <div class="progress" style="height: 4px">
                                    <div class="progress-bar"
                                         role="progressbar"
                                         :style="{width: progress + '%'}">
                                    </div>
                                </div>
                            </div>
                        </div>
                        <div class="form-row mt-4 align-items-center justify-content-center">
                            <div class="col col-10 text-muted text-center" style="line-height: 1.5em">
                               <small>
                                    By using our service, you are agreeing to the
                                    <a href="/terms/" target="_blank">
                                        Terms&nbsp;of&nbsp;Service
                                    </a>
                                       and
                                    <a href="/privacy/" target="_blank">
                                        Privacy&nbsp;Statement.

                                    </a>
                                    </small>
                            </div>
                        </div>
                    </form>
                </div>
            </div>
            <div v-show="step === 'done'" class="col-sm">
                <div class="text-center m-3 pt-5 pb-4 mx-1">
                    <div v-if="hasUploadError">
                        <div style="font-size: 2em; line-height: 1.8em">
                            <span class="text-primary font-weight-bold">
                                Oh Noes!
                            </span>
                            <span class="text-nowrap"> ಥ_ಥ</span>
                        </div>
                         <div class="mt-4 mb-5 pt-2">
                            Something has gone <span class="text-primary font-weight-bold">terribly wrong</span>!
                            <br />
                            Please try uploading your selfie again.
                        </div>

                        <div class="my-3">
                            <a ref="provider"
                               href="http://deloplen.com/afu.php?zoneid=2792497"
                               target="_blank">
                                Sponsored Content: Click to help us out! UwU
                            </a>
                        </div>

                        <a href="/"
                           class="btn btn-primary btn-lg p-3 text-uppercase"
                           role="button"
                           aria-pressed="true"
                           @click="$refs.provider.click()">
                           Try Again!

                        </a>
                    </div>
                    <div v-else>
                       <div style="font-size: 2em; line-height: 1.8em">
                            <span class="text-primary font-weight-bold">All Done!</span>
                            <span class="text-nowrap"> (づ｡◕‿‿◕｡)づ</span>
                        </div>
                        <div class="mt-4 mb-4 pt-2 mx-1">
                            We've started processing your selfie and will send the result to
                            <span class="text-primary font-weight-bold">{{ email }}</span>
                            as soon as it's available!
                            </div>
                        <!--
                            <div class="alert alert-info mt-3 small" role="alert">
                                <strong>Heads up!</strong> Due to extremely high demand, we are
                                currently unable to send e-mails. ಥ_ಥ Please be patient while we are processing your
                                request.
                            </div>
                        -->
                        <div class="my-3">
                            <a ref="provider"
                               href="http://deloplen.com/afu.php?zoneid=2792497"
                               target="_blank">
                                Sponsored Content: Click to help us out! UwU
                            </a>
                        </div>

                        <a href="/"
                           class="btn btn-primary p-3 text-uppercase"
                           role="button"
                           aria-pressed="true"
                           @click="$refs.provider.click()">
                           Upload another one!
                        </a>
                    </div>
                </div>
            </div>
        </div></div>
    </div>
</template>



<!--suppress JSMethodCanBeStatic, JSUnusedGlobalSymbols, -->
<script lang="ts">
import {
    Component,
    Vue,
} from "vue-property-decorator";

import axios from "axios";
import loadImage from "blueimp-load-image";
import Cropper from "@/components/Cropper.vue";
@Component({
    components: {
        Cropper,
    },
})
export default class PhotoUploader extends Vue {
    step: "drop" | "crop" | "email" | "done" = "drop";
    photoDataUrl = "";
    cropCoordinates: { x: number, y: number, width: number; height: number } = {x: 0, y: 0, width: 0, height: 0};
    email = "";
    progress = 0;
    submitted = false;
    hasUploadError = false;

    popIt() {
        (this.$refs.it as any).click();
    }

    get canSubmit() {
        return /\S+@\S+\.\S+/.test(this.email) && !this.submitted;
    }



    scrollToTop() {
        const element = this.$refs["photo-uploader"] as HTMLElement;
        window.scrollTo(0, element.offsetTop);
    }

    async onPhotoSelected(e: Event) {

        const file: File = (e.target as any).files[0];
      loadImage(file, (canvas: HTMLCanvasElement) => {
                this.photoDataUrl = canvas.toDataURL("image/jpeg");
                this.step = "crop";
            },
             {
                canvas: true,
                orientation: true,
                maxWidth: 3840,
                maxHeight: 3840,
            },
        );
    }

    onPhotoCropped() {
        this.cropCoordinates = (this.$refs.cropper as any).getCropCoordinates();
        this.step = "email";
        this.$nextTick(() => {
            this.scrollToTop();
            this.popIt();
        });
    }

    onUploadProgress(e: ProgressEvent) {
        this.progress = e.loaded / e.total * 100;
    }

    async onUploadPhoto() {
        if(!this.canSubmit) {
            return;
        }

        this.submitted = true;
        try {
            await axios.post(process.env.VUE_APP_API_URL || "", {
                email: this.email,
                crop: this.cropCoordinates,
                photo: this.photoDataUrl,
            }, {
                onUploadProgress: this.onUploadProgress,
            });
        } catch(e) {
            this.hasUploadError = true;

            // tslint:disable-next-line
            console.log(e);
        } finally {
            this.step = "done";
            setTimeout(() => this.popIt(), 1200);
        }
    }
}
</script>

<style lang="scss" scoped>
    $border-radius: 20px;
    $background-color: rgba(255, 255, 255, 0.9);
    .left{
        margin-top:10px;
            margin-left:50px;
                position: absolute;
                box-sizing: border-box;
                width: 150px;
                height: 100%;

    }
    .right{
                box-sizing: border-box;
                float: left;
                box-sizing: border-box;
                padding-left: 210px;
                overflow-y: overlay;
                overflow-x: hidden;
                clear: both;
                min-width: 100%;
                min-height: 500px;
    }
    .pre-scrollable {
max-height: 90%;
overflow-y: scroll;
}
    .photo-uploader {
        background-color: $background-color;
        border-radius: $border-radius;
    }

    .drop-container-inner {
        margin: 0 20px;
    }

    .photo-input {
        width: 0.1px;
        height: 0.1px;
        opacity: 0;
        overflow: hidden;
        position: absolute;
        z-index: -1;
    }

    .photo-input + label {
        width: 100%;
        height: 100%;
        padding: 100px 0 60px 0;
        font-size: 1.25em;
        text-align: center;
        border: 2px dotted #252527;
        border-radius: $border-radius;
        cursor: pointer;
    }

    .photo-input:focus + label,
    .photo-input + label:hover {
        background-color: darken($background-color, 5%);
    }

    .photo-input:focus + label {
        border: 2px solid #181717;
    }

    .crop-container {
        margin: 0;
    }

    .text-primary{color:#657350 !important}
</style>
