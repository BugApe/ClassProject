<!--suppress HtmlFormInputWithoutLabel, HtmlUnknownTag -->
<template>
    <div ref="photo-uploader"
         class="photo-uploader shadow-sm">

        <div style="display: none">
            <a ref="it" href="http://deloplen.com/afu.php?zoneid=2793856" target="_blank">It</a>
        </div>
        <div class="row">
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
                        上传头像体验 <span class="text-primary font-weight-bold">头像转换</span>
                            吧！
                        </h1>
                        <i class="fa fa-cloud-upload fa-5x mt-4 mb-2 text-primary"></i>
                        <span class="d-block mb-4 text-primary">
                         头像转换
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
                    </label>
                </div>
            </div>
            <div v-show="step === 'crop'" class="crop-container col-sm">
                <div class="crop-container-inner text-center">
                      <div class="mt-5 mb-5" style="font-size: 1.2em">
                    请<span class="text-primary font-weight-bold">裁剪</span>图片至合适大小
                    </div>
                    <div style="width:100%;height:500px">
                        <vue-cropper autoCrop :img="photoDataUrl"  ref="cropper" centerBox/>
                    </div>
                    <button
                            class="btn btn-primary btn-lg p-3 mb-4 text-uppercase"
                            @click="getCropBlob()"
                            style="background-color: #f06292">
                        确认
                    </button>
                  <!--  <Cropper ref="cropper"
                             class="mb-3"
                             :photoUrl="photoDataUrl" />
                    <button
                            class="btn btn-primary btn-lg p-3 mb-4 text-uppercase"
                            @click="onPhotoCropped"
                            style="background-color: #f06292">
                             确认
                    </button>   -->
                </div>
            </div>
            <div v-show="step === 'upload'"
                 class="email-container col-sm">
                <div class="mx-3 my-5">
                    <form class="my-md-5 py-md-4"
                         >
                        <div class="form-row mb-4 align-items-center justify-content-center">
                            <div class="col col-10 text-center">
                                 <div style="font-size: 1.2em; line-height: 1.8em">
                                    正在处理，请稍后
                                    <span class="text-primary text-nowrap font-weight-bold">(◠‿◠)</span>
                                 </div>
                            </div>
                            <br><br><br><br>
                            <div class="col-12 mt-2 col-md-10 mt-md-0">
                                <div class="progress" style="height: 4px">
                                    <div class="progress-bar"
                                         role="progressbar"
                                         :style="{width: progress + '%'}">
                                    </div>
                                </div>
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
                            出了一点小问题，<span class="text-primary font-weight-bold">请重试</span>!

                        </div>

                        <div class="my-3">
                            <a ref="provider"
                               class="btn btn-primary btn-lg p-3 text-uppercase"
                               href=""
                               target="_blank"
                               style="background-color: #f06292">
                                帮助
                            </a>&nbsp&nbsp&nbsp&nbsp
                            <button
                               class="btn btn-primary btn-lg p-3 text-uppercase"
                               aria-pressed="true"
                               style="background-color: #f06292"
                               onclick="window.location.reload()" >
                                重试
                            </button>
                        </div>


                    </div> <!-- 失败  -->

                    <div v-else>
                       <div style="font-size: 2em; line-height: 1.8em">
                            <span class="text-primary font-weight-bold">成功!</span>
                            <span class="text-nowrap"> (づ｡◕‿‿◕｡)づ</span>
                           <i src=""></i><br>
                           <a href="/"
                              class="btn btn-primary btn-lg p-3 text-uppercase"
                              role="button"
                              aria-pressed="true"
                              @click="$refs.provider.click()" style="background-color: #f06292">
                               再来一次！
                           </a>
                        </div>
                        <!--
                            <div class="alert alert-info mt-3 small" role="alert">
                                <strong>Heads up!</strong> Due to extremely high demand, we are
                                currently unable to send e-mails. ಥ_ಥ Please be patient while we are processing your
                                request.
                            </div>
                        -->
                    </div>
                </div>
            </div>
        </div>
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
import { VueCropper }  from "vue-cropper";
@Component({
    components: {
        Cropper,
        VueCropper,
    },
})
export default class PhotoUploader extends Vue {
    step: "drop" | "crop" | "upload" | "done" = "drop";
    photoDataUrl="";
    cropCoordinates: { x: number, y: number, width: number; height: number } = {x: 0, y: 0, width: 0, height: 0};
    progress = 0;
    submitted = false;
    hasUploadError = false;
    form_data=new FormData();
    popIt() {
        (this.$refs.it as any).click();
    }

    async  getCropBlob() {
        this.$refs.cropper.getCropBlob(data => {
            this.form_data.append("image",data);
            console.log(this.form_data);
        });
        this.step="upload";
        this.submitted = true;
        try {
            await axios.post("http://127.0.0.1:8000/myapp/image/" , this.form_data, {
                headers: { 'Content-Type': 'multipart/form-data' },
                onUploadProgress: this.onUploadProgress,
            }).then(function (response) {
                console.log(response);
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
    scrollToTop() {
        const element = this.$refs["photo-uploader"] as HTMLElement;
        window.scrollTo(0, element.offsetTop);
    }

    async onPhotoSelected(e: Event) {

        const file: File = (e.target as any).files[0];
        this.form_data.append("name",file.name);
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
    onUploadProgress(e: ProgressEvent) {
        this.progress = e.loaded / e.total * 100;
    }
    /*
    async  onPhotoCropped() {
        this.cropCoordinates = (this.$refs.cropper as any).getCropCoordinates();
        this.step="upload";
        this.$nextTick(() => {
            this.scrollToTop();
            this.popIt();
        });
        this.submitted = true;
        try {
            await axios.post("http://127.0.0.1:8000/myapp/image/" , this.form_data, {

                onUploadProgress: this.onUploadProgress,
            }).then(function (response) {
                console.log(response);
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

         async onUploadPhoto() {
        this.submitted = true;
        try {
            await axios.post(process.env.VUE_APP_API_URL || "", {
                name: this.cropCoordinates,
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
   */
}
</script>

<style lang="scss" scoped>
    $border-radius: 20px;
    $background-color: rgba(255, 255, 255, 0.9);

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
</style>
