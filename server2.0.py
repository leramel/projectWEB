from flask import Flask

app = Flask(__name__)


@app.route('/')
def index():
    return """"<!DOCTYPE html>
<!-- This website/webapp was created in Softr. https://www.softr.io -->
<!-- Last Published: Tue, April 25 2023 09:35:02 -->
<html lang="en">
    <head>

        <meta charset="utf-8">
        <meta http-equiv="X-UA-Compatible" content="IE=edge">
        <meta name="viewport" content="user-scalable=no, initial-scale=1, maximum-scale=1, minimum-scale=1, width=device-width, height=device-height, target-densitydpi=device-dpi, shrink-to-fit=no" />

        <script>
            const reactDefaultThemes = {defaultBaseTextSize: '16px',defaultBodyFont: 'Inter',defaultBodyFontWeight: '300',defaultBodyTextColor: '#383B3D',defaultButtonBackgroundColor: '#212121',defaultButtonRoundness: '.5rem',defaultButtonTextColor: '#ffffff',defaultContainerStyle: 'container',defaultTitleFont: 'Inter',defaultTitleFontWeight: '600',defaultTitleTextColor: '#383B3D'};
        </script>

        <meta name="twitter:title" content="Home"><meta property="twitter:title" content="Home"><meta property="og:title" content="Home">
        
        

        <title>Школьная столовая</title>
        
        
        

        <link rel="icon" type="image/x-icon" href="https://softr-prod.imgix.net/applications/8f7af9fb-a550-425d-b327-48195c193a5f/assets/c870e998-d79a-414a-8577-5bb4e5b7464d.svg?rnd=1622671497214" />

        
        <link rel="canonical" href="https://schoiolcan.preview.softr.app/" />
        <link href="https://fonts.softr-files.com/google/api/css?family=Inter:100,200,300,500,600,600,700,800,900,400&display=swap" rel="stylesheet">

        <link href="https://assets.softr-files.com/libs/bootstrap/4.3.1/css/bootstrap.min.css" rel="stylesheet">
        <link href="https://assets.softr-files.com/libs/font-awesome/5.14.0/css/all.min.css" rel="stylesheet">

        <style type="text/css">

            html {
                scroll-behavior: smooth;
                font-size: 16px;
                overflow-x: hidden;
            }

            body {
              overflow-x: hidden;
            }

            .container {
                max-width: 100%;
            }

            @media (min-width: 576px) {
                .container {
                    max-width: 540px;
                }
            }

            @media (max-width: 576px) {
                .navbar-brand img {
                    max-width: 15rem!important;
                }
            }

            @media (min-width: 768px) {
                .container {
                    max-width: 720px;
                }
            }

            @media (min-width: 992px) {
                .container {
                    max-width: 960px;
                }
            }

            @media (min-width: 1200px) {
                .container {
                    max-width: 1140px;
                }
            }

            p, h1, h2, h3, h4, h5, small { white-space: pre-line; }

            @media screen and (max-width: 768px) {
              input, select, textarea {
                font-size: 16px !important;
              }
            }

            h1.sw-font-family-default,
            h2.sw-font-family-default {
                font-family: "Inter";
            }

            h1.sw-font-weight-default,
            h2.sw-font-weight-default {
                font-weight: 600;
            }

            h1.sw-text-color-default,
            h2.sw-text-color-default {
                color: #383B3D;
            }

            section.sw-font-family-default,
            header.sw-font-family-default,
            nav.sw-font-family-default,
            footer.sw-font-family-default,
            div.sw-font-family-default,
            span.sw-font-family-default,
            small.sw-font-family-default,
            pre.sw-font-family-default,
            p.sw-font-family-default,
            b.sw-font-family-default,
            li.sw-font-family-default,
            ul.sw-font-family-default,
            a.sw-font-family-default,
            h3.sw-font-family-default,
            h4.sw-font-family-default,
            h5.sw-font-family-default,
            h6.sw-font-family-default {
                font-family: "Inter";
            }

            span.sw-font-weight-default,
            li.sw-font-weight-default span,
            small.sw-font-weight-default,
            li.sw-font-weight-default small,
            pre.sw-font-weight-default,
            p.sw-font-weight-default,
            h3.sw-font-weight-default,
            h4.sw-font-weight-default,
            h5.sw-font-weight-default,
            h6.sw-font-weight-default {
                font-weight: 300;
            }

            span.sw-text-color-default,
            li.sw-text-color-default span,
            small.sw-text-color-default,
            li.sw-text-color-default small,
            pre.sw-text-color-default,
            p.sw-text-color-default,
            div.sw-text-color-default,
            h3.sw-text-color-default,
            h4.sw-text-color-default,
            h5.sw-text-color-default,
            h6.sw-text-color-default {
                color: #383B3D;
            }

            input.sw-font-family-default,
            textarea.sw-font-family-default {
                font-family: "Inter";
            }

            input.sw-font-weight-default,
            textarea.sw-font-weight-default {
                font-weight: 300;
            }

            .sw-font-family-default::-webkit-input-placeholder,
            .sw-font-family-default::-moz-placeholder,
            .sw-font-family-default:-ms-input-placeholder,
            .sw-font-family-default:-moz-placeholder {
                font-family: "Inter";
            }

            .sw-font-family-default::-webkit-input-placeholder,
            .sw-font-family-default::-moz-placeholder,
            .sw-font-family-default:-ms-input-placeholder,
            .sw-font-family-default:-moz-placeholder {
                font-weight: 300;
            }

            .sw-text-color-default[data-element='button'] {
                color: #ffffff;
            }

            .sw-background-color-default[data-element='button'] {
                background-color: #212121;
            }

            .sw-border-radius-default[data-element='button'] {
                border-radius: .5rem;
            }

            /* Micromodal styles */
            .sw-modal {
                display: none;
            }

            .sw-modal.is-open {
                display: block;
            }

            .sw-modal .sw-modal-overlay {
                position: fixed;
                top: 0;
                left: 0;
                right: 0;
                bottom: 0;
                background: rgba(0, 0, 0, 0.6);
                display: flex;
                justify-content: center;
                align-items: center;
                z-index: 9999;
            }

            .sw-modal .sw-modal-container {
                background-color: #FFFFFF;
                padding: 40px 10px 10px 10px;
                overflow-y: auto;
                box-sizing: border-box;
                position: relative;
                margin: auto;
                border-radius: 16px;
            }

            .sw-modal #sw-modal-content {
                display: flex;
                align-items: center;
                justify-content: center;
            }

            .sw-modal .sw-modal-close {
                background: transparent;
                border: 0;
                position: absolute;
                right: 10px;
                top: 10px;
            }

            .sw-modal-close:focus {
                outline: none;
            }

            .sw-modal .sw-modal-iframe {
                border: none;
            }

            .sw-modal-size-sm {
                width: 464px;
                height: 350px;
                max-width: 95vw;
                max-height: 95vh;
            }


            .sw-modal-size-md {
                width: 755px;
                height: 600px;
                max-width: 95vw;
                max-height: 95vh;
            }

            .sw-modal-size-lg {
                width: 1196px;
                height: 780px;
                max-width: 95vw;
                max-height: 95vh;
            }

            .sw-modal-size-xl {
                width: 95vw;
                height: 95vh;
            }

            .sw-modal-container > div, #sw-modal-content, #sw-modal-content iframe {
                width: 100%;
                height: 100%;
            }

            .sw-modal-close:before {
                content: "\2715";
            }

            @keyframes rotation {
                from {
                    transform: rotate(0deg);
                }
                to {
                    transform: rotate(359deg);
                }
            }

            .sw-font-size-m { font-size: 1rem!important; } .sw-text-color-default {  } .sw-font-family-default {  } .sw-font-weight-medium { font-weight: 500!important; } .sw-background-color-f9fafb { background-color: #f9fafb!important; } .sw-letter-spacing-normal { letter-spacing: 0rem!important; } .sw-padding-left-4xs { padding-left: 1rem!important; } .sw-padding-top-4xs { padding-top: 1rem!important; } .sw-padding-bottom-4xs { padding-bottom: 1rem!important; } .sw-text-decoration-no-underline { text-decoration: none!important; } .sw-display-block { display: block!important; } .sw-border-bottom-style-solid { border-bottom-style: solid!important; } .sw-border-bottom-width-xs { border-bottom-width: 1px!important; } .sw-border-bottom-color-f1f2f3 { border-bottom-color: #f1f2f3!important; } .sw-cursor-pointer { cursor: pointer!important; } .sw-font-weight-normal { font-weight: 400!important; } .sw-background-color-ffffff { background-color: #ffffff!important; } .sw-line-height-normal { line-height: 1.5!important; } .sw-padding-right-4xs { padding-right: 1rem!important; } .sw-margin-bottom-none { margin-bottom: 0rem!important; } .sw-padding-top-2xl { padding-top: 6rem!important; } .sw-padding-bottom-2xl { padding-bottom: 6rem!important; } .sw-border-top-style-none { border-top-style: none!important; } .sw-border-top-width-xs { border-top-width: 1px!important; } .sw-border-top-color-000000 { border-top-color: #000000!important; } .sw-border-bottom-style-none { border-bottom-style: none!important; } .sw-border-bottom-color-000000 { border-bottom-color: #000000!important; } .sw-font-size-4xl { font-size: 2.25rem!important; } .sw-font-weight-default {  } .sw-padding-top-none { padding-top: 0rem!important; } .sw-font-size-xl { font-size: 1.25rem!important; } .sw-padding-bottom-3xs { padding-bottom: 1.25rem!important; }   #faq1 .sw-accordion-border {  border: 1px solid #f1f2f3; }  #faq1 .arrow {  position: absolute;  right: 39px;  display: inline-block;  width: 6px;  height: 6px;  border-left: 1px solid #29394c;  border-top: 1px solid #29394c;  transform: rotate(45deg);  transition: .2s linear;  margin-top: 10px; }  #faq1 .collapsed .arrow {  transform: rotate(-135deg); }
.sw-font-size-m { font-size: 1rem!important; } .sw-text-color-default {  } .sw-font-family-default {  } .sw-font-weight-medium { font-weight: 500!important; } .sw-background-color-f9fafb { background-color: #f9fafb!important; } .sw-letter-spacing-normal { letter-spacing: 0rem!important; } .sw-padding-left-4xs { padding-left: 1rem!important; } .sw-padding-top-4xs { padding-top: 1rem!important; } .sw-padding-bottom-4xs { padding-bottom: 1rem!important; } .sw-text-decoration-no-underline { text-decoration: none!important; } .sw-display-block { display: block!important; } .sw-border-bottom-style-solid { border-bottom-style: solid!important; } .sw-border-bottom-width-xs { border-bottom-width: 1px!important; } .sw-border-bottom-color-f1f2f3 { border-bottom-color: #f1f2f3!important; } .sw-cursor-pointer { cursor: pointer!important; } .sw-font-weight-normal { font-weight: 400!important; } .sw-background-color-ffffff { background-color: #ffffff!important; } .sw-line-height-normal { line-height: 1.5!important; } .sw-padding-right-4xs { padding-right: 1rem!important; } .sw-margin-bottom-none { margin-bottom: 0rem!important; } .sw-padding-top-2xl { padding-top: 6rem!important; } .sw-padding-bottom-2xl { padding-bottom: 6rem!important; } .sw-border-top-style-none { border-top-style: none!important; } .sw-border-top-width-xs { border-top-width: 1px!important; } .sw-border-top-color-000000 { border-top-color: #000000!important; } .sw-border-bottom-style-none { border-bottom-style: none!important; } .sw-border-bottom-color-000000 { border-bottom-color: #000000!important; } .sw-font-size-4xl { font-size: 2.25rem!important; } .sw-font-weight-default {  } .sw-padding-top-none { padding-top: 0rem!important; } .sw-font-size-xl { font-size: 1.25rem!important; } .sw-padding-bottom-3xs { padding-bottom: 1.25rem!important; }   #faq2 .sw-accordion-border {  border: 1px solid #f1f2f3; }  #faq2 .arrow {  position: absolute;  right: 39px;  display: inline-block;  width: 6px;  height: 6px;  border-left: 1px solid #29394c;  border-top: 1px solid #29394c;  transform: rotate(45deg);  transition: .2s linear;  margin-top: 10px; }  #faq2 .collapsed .arrow {  transform: rotate(-135deg); }
.sw-font-size-m { font-size: 1rem!important; } .sw-text-color-default {  } .sw-font-family-default {  } .sw-font-weight-default {  } .sw-border-radius-default {  } .sw-background-color-default {  } @media (hover: hover) { .hover\:sw-background-color-default:hover {  } } @media (hover: hover) { .hover\:sw-box-shadow-s:hover { box-shadow: 0px 0px 6px 0px rgba(17, 17, 17, 0.04), 0px 4px 8px 0px rgba(17, 17, 17, 0.04)!important; } } .sw-padding-left-xs { padding-left: 2rem!important; } .sw-padding-right-xs { padding-right: 2rem!important; } .sw-padding-top-5xs { padding-top: 0.75rem!important; } .sw-padding-bottom-5xs { padding-bottom: 0.75rem!important; } .sw-margin-top-none { margin-top: 0rem!important; } .sw-margin-bottom-none { margin-bottom: 0rem!important; } .sw-border-style-none { border-style: none!important; } .sw-border-width-xs { border-width: 1px!important; } .sw-border-color-000000 { border-color: #000000!important; } @media (hover: hover) { .hover\:sw-border-color-000000:hover { border-color: #000000!important; } } .sw-letter-spacing-normal { letter-spacing: 0rem!important; } .sw-text-decoration-no-underline { text-decoration: none!important; } @media (hover: hover) { .hover\:sw-text-decoration-no-underline:hover { text-decoration: none!important; } } .sw-font-size-s { font-size: 0.875rem!important; } .sw-text-color-#007bff { color: ##007bff!important; } .sw-font-weight-medium { font-weight: 500!important; } .sw-padding-top-6xs { padding-top: 0.5rem!important; } .sw-padding-bottom-6xs { padding-bottom: 0.5rem!important; } .sw-background-color-FAFAFC { background-color: #FAFAFC!important; } @media (hover: hover) { .hover\:sw-background-color-FAFAFC:hover { background-color: #FAFAFC!important; } } .sw-text-color-212121 { color: #212121!important; } .sw-border-radius-l { border-radius: 0.5rem!important; } .sw-margin-top-6xs { margin-top: 0.5rem!important; } .sw-margin-bottom-6xs { margin-bottom: 0.5rem!important; } .sw-border-style-solid { border-style: solid!important; } .sw-border-color-F0F0F4 { border-color: #F0F0F4!important; } @media (hover: hover) { .hover\:sw-border-style-solid:hover { border-style: solid!important; } } @media (hover: hover) { .hover\:sw-border-width-xs:hover { border-width: 1px!important; } } @media (hover: hover) { .hover\:sw-border-color-AEAEB5:hover { border-color: #AEAEB5!important; } } .sw-box-shadow-none { box-shadow: none!important; } .sw-display-inline-block { display: inline-block!important; } .sw-padding-left-4xs { padding-left: 1rem!important; } .sw-outline-none { outline: none!important; } .sw-width-full { width: 100%!important; } .sw-border-radius-m { border-radius: 0.25rem!important; } .sw-background-color-ffffff { background-color: #ffffff!important; } .sw-padding-top-2xl { padding-top: 6rem!important; } .sw-padding-bottom-2xl { padding-bottom: 6rem!important; } .sw-border-top-style-none { border-top-style: none!important; } .sw-border-top-width-xs { border-top-width: 1px!important; } .sw-border-top-color-000000 { border-top-color: #000000!important; } .sw-border-bottom-style-none { border-bottom-style: none!important; } .sw-border-bottom-width-xs { border-bottom-width: 1px!important; } .sw-border-bottom-color-000000 { border-bottom-color: #000000!important; } .sw-width-6xs { width: 7rem!important; } .sw-padding-top-none { padding-top: 0rem!important; } .sw-padding-bottom-xs { padding-bottom: 2rem!important; } @media (hover: hover) { .hover\:sw-box-shadow-none:hover { box-shadow: none!important; } } .sw-border-color-E5E5EA { border-color: #E5E5EA!important; } @media (hover: hover) { .hover\:sw-border-color-212121:hover { border-color: #212121!important; } } .sw-background-repeat-no-repeat { background-repeat: no-repeat!important; } .sw-background-size-cover { background-size: cover!important; } .sw-background-position-center { background-position: center!important; } .sw-background-attachment-scroll { background-attachment: scroll!important; } .sw-font-size-2xl { font-size: 1.5rem!important; } .sw-padding-bottom-4xs { padding-bottom: 1rem!important; } .sw-line-height-normal { line-height: 1.5!important; } .sw-border-width-none { border-width: 0px!important; } .sw-border-color-eaeced { border-color: #eaeced!important; } .sw-border-radius-2xl { border-radius: 1rem!important; } .sw-box-shadow-l { box-shadow: 0px 2px 4px 0px rgba(17, 17, 17, 0.04), 0px 8px 32px 0px rgba(33, 33, 33, 0.08)!important; } .sw-text-color-383B3D { color: #383B3D!important; } @media (hover: hover) { .hover\:sw-background-color-ffffff:hover { background-color: #ffffff!important; } } .sw-margin-top-4xs { margin-top: 1rem!important; }  #user-accounts1 .btn {      background: transparent;      border: none;     }  #user-accounts1 #sw-form-password-input{  background: transparent;     } #user-accounts1 #sw-form-terms-input, #user-accounts1 #sw-form-remember-input{  width: 16px;  height: 16px;  border-radius: 0;  margin-right: 10px; }  #user-accounts1 .sw-btn-success {  background: #24A37D !important;  color: #fff !important; } #user-accounts1 .link  {  cursor: pointer; } #user-accounts1 .form  {  width: 450px; }  #user-accounts1 .error-message  {      display: none;      color: #5A5D63;      right: 0;      justify-content: flex-start;      padding: 5px;      width: 100%;      font-size: 11px;      font-weight: 500;      margin-bottom: 5px;      align-items: flex-start;     } #user-accounts1 .error-message  img{    margin-right: 5px;     } #user-accounts1 #signup  {    padding: 40px;     }  #user-accounts1 .loginSignUpSeparator, #user-accounts1 .loginSignUpSeparator-google{      border-top: 1px solid #cbd2d6;      position: relative;      margin: 20px 20px 0;      text-align: center;      width: 100%;     }  #user-accounts1 .loginSignUpSeparator-google {      margin: 30px 0 10px;     }  #user-accounts1 .loginSignUpSeparator .textInSeparator, #user-accounts1 .loginSignUpSeparator-google .textInSeparator{      background-color: #fff;      padding: 0 .5em;      position: relative;      color: #6c7378;      top: -.9em;     }  #user-accounts1 .sw-btn-success .fa-check {  display: inline-block !important;  color: #fff !important;  position: relative !important;  left: 0.5rem !important; } #user-accounts1 .sw-input-invalid {      border: 1px solid #E25B5B !important;     }  #user-accounts1 .sw-invalid-checkbox ~ .checkmark {  border: 1px solid #E25B5B!important; }  #user-accounts1 #sw-form-password-input.sw-input-invalid, #user-accounts1 .sw-time-input.sw-input-invalid{  border: none !important; }  #user-accounts1 .sw-btn-spinner {  width: 1rem !important;  height: 1rem !important;  margin-left: 0.5rem !important; }  #user-accounts1 .password i{      position: relative;      cursor: pointer;      color: #00000056;      right: 15px;     } #user-accounts1 .password input{      width: 100%;      padding: 0;      margin: 0;      border: 0;     } #user-accounts1 .password input:focus{      outline: none;     }  #user-accounts1 .validation-message{  color: #5A5D63;  font-weight: 500;  font-size: 11px;  margin-top: -5px;  margin-bottom: 10px; }  #user-accounts1 .password i.active{      color: #000000;     }  #user-accounts1 .checkbox-container input {      position: absolute;      opacity: 0;      cursor: pointer;      height: 0;      width: 0;     }  #user-accounts1 .checkbox-container .checkmark:after {      content: "";      position: absolute;      display: none;      border: solid #495057;      border-width: 0 2px 2px 0;      -webkit-transform: rotate(45deg);      -ms-transform: rotate(45deg);      transform: rotate(45deg);     }  #user-accounts1 .checkbox-container input:checked ~ .checkmark:after {      display: block;     } #user-accounts1 .checkbox-container .sw-checkbox  {      min-height: 20px!important;      min-width: 20px!important;      padding: 0!important;      border: 1px solid #E5E5EA;      margin-right: 8px;     } #user-accounts1 .checkbox-container .sw-checkbox:after {      left: 7px;      top: 3px;      width: 5px;      height: 11px;     }  #user-accounts1 .checkbox-container {    display: block;    position: relative;    cursor: pointer;    font-size: 22px;     }  #user-accounts1 .checkbox-container input {    position: absolute;    opacity: 0;    cursor: pointer;    height: 0;    width: 0;     }   #user-accounts1 .checkbox-container .checkmark:after {    content: "";    position: absolute;    display: none;    border: solid #000;    border-width: 0 2px 2px 0;    -webkit-transform: rotate(45deg);    -ms-transform: rotate(45deg);    transform: rotate(45deg);     }  #user-accounts1 .checkbox-container input:checked ~ .checkmark:after {    display: block;     } #user-accounts1 .checkbox-container .sw-checkbox-s  {    min-height: 20px!important;    min-width: 20px!important;    padding: 0!important;     } #user-accounts1 .checkbox-container .sw-checkbox-s:after {    left: 7px;    top: 3px;    width: 5px;    height: 11px;     } #user-accounts1 .checkbox-container .sw-checkbox-m  {    min-height: 30px!important;    min-width: 30px!important;    padding: 0!important;     } #user-accounts1 .checkbox-container .sw-checkbox-m:after {    left: 11px;    top: 8px;    width: 6px;    height: 12px;     } #user-accounts1 .checkbox-container .sw-checkbox-l  {    min-height: 40px!important;    min-width: 40px!important;    padding: 0!important;     } #user-accounts1 .checkbox-container .sw-checkbox-l:after {    left: 16px;    top: 12px;    width: 6px;    height: 14px;     } #user-accounts1 .checkbox-container .sw-checkbox-s.sw-input-invalid:after  {    left: 6px;    top: 2px;     } #user-accounts1 .checkbox-container .sw-checkbox-m.sw-input-invalid:after  {    top: 6px;     }   #user-accounts1 input:-webkit-autofill {      animation-name: onAutoFillStart;      transition: background-color 50000s ease-in-out 0s;     } #user-accounts1 input:not(:-webkit-autofill) {      animation-name: onAutoFillCancel;     }  #user-accounts1 .bootstrap-select .btn:focus {    outline: none !important;     }  #user-accounts1 .cursor-pointer {    cursor: pointer;     }  #user-accounts1 .bootstrap-select .btn-light {    padding-left: 0;    padding-top: 0;    padding-bottom: 0;    font-size: inherit !important;    display: flex;    color: inherit;     }  #user-accounts1 .dropdown .dropdown-menu {    left: -12px!important;     }  #user-accounts1 .sw-date-field .dropdown .dropdown-menu {    left: 12px!important;     }  #user-accounts1 .bootstrap-select div.dropdown-menu div.show {    transform: none !important;     }  #user-accounts1 .bootstrap-select .btn-light:focus {    box-shadow: none !important;     }  #user-accounts1 .bootstrap-select .btn-light:after {    color: #000;     }  #user-accounts1 .bootstrap-select .dropdown-menu {    font-size: inherit;    color: inherit;     } #user-accounts1 .sw-date-field .bootstrap-select .dropdown-menu {    min-width: 130px;    max-width: 130px;     }  #user-accounts1 .bootstrap-select .dropdown-item.active, .dropdown-item:active {    color: #000000;    text-decoration: none;    background-color: #ffffff;     }  #user-accounts1 .bootstrap-select .dropdown-item {    color: inherit!important;     }  #user-accounts1 .bootstrap-select .dropdown-item:focus {    outline: none;    border: none;     }  /* IE11 hide native button (thanks Matt!) */ #user-accounts1 select::-ms-expand {    display: none;     } #user-accounts1 select {    text-indent: 1px;    text-overflow: '';    width: 100px;    -webkit-appearance: none;    -moz-appearance: none;    appearance: none;    padding: 2px 2px 2px 2px;    border: none;    background: url("https://softr-assets-eu-shared.s3.eu-central-1.amazonaws.com/studio/blocks/assets/chevron-down-small.svg") white no-repeat calc(100% - 10px) !important;     }   #user-accounts1 .sw-btn-success {    background: #24A37D !important;    color: #fff !important;     }   #user-accounts1 .sw-btn-success .fa-check {    display: inline-block !important;    color: #fff !important;    position: relative !important;    left: 0.5rem !important;     }   #user-accounts1 .sw-btn-spinner {    width: 1rem !important;    height: 1rem !important;    margin-left: 0.5rem !important;     }  #user-accounts1 .drag{    padding-right: 12px!important;     } #user-accounts1 .drag .upload-header{    font-size: 14px;    font-weight: 500;    font-stretch: normal;    font-style: normal;    line-height: 1.71;    letter-spacing: normal;    color: #adadad;     } #user-accounts1 .drag .upload-header i{    color: #373737;     } #user-accounts1 .drag-file-area {    display: flex;    flex: 1;    justify-content: center;    align-items: center;    border: dashed 1px #979797;    background-color: rgba(255, 255, 255, 0.04);    margin: 12px 0;    border-radius: 2px;     } #user-accounts1 .drag-file-area .drag-text {    display: flex;     } #user-accounts1 .drag-file-area .drag-text span {    display: flex;    flex-direction: column;    align-items: center;    margin: 0;    font-size: 12px;    font-weight: 500;    font-stretch: normal;    font-style: normal;    line-height: 1.33;    letter-spacing: normal;    color: #adadad;    padding: 28px 0;     }  #user-accounts1 .file-input {    display: none;     } #user-accounts1 .browse-link {    color: #18a0fb;    font-size: 12px;    margin-left: 4px;    cursor: pointer;     } #user-accounts1 .browse-link:focus {    outline: none;     }  #user-accounts1 .file-list {    margin: 12px 0;    flex: 1;    overflow: auto;    list-style-type: none;    padding: 28px 0;    border: dashed 1px #979797;     }  #user-accounts1 .file-list  li {    font-size: 12px;    font-weight: 500;    font-stretch: normal;    font-style: normal;    line-height: 1.33;    letter-spacing: normal;    color: #adadad;    position: relative;    padding: 0 12px;    margin-bottom: 16px;     } #user-accounts1 .file-list li div{    display: flex;    justify-content: space-between;     } #user-accounts1 .delete {    position: absolute;    right: 10px;    top: -2px;    padding: 5px;    color: #373737;    text-align: center;    line-height: 15px;    z-index: 1;    cursor: pointer;    display: block;    width: 20px;    height: 20px;     } #user-accounts1 .progressbar {    display: block;    height: 4px;    border-radius: 2px;    background-color: rgba(0, 0, 0, 0.4);    width: 100%;    margin-top: 6px;     } #user-accounts1 .blink {    background-image: linear-gradient(90deg, #f1f1f1 0px, rgb(225, 225, 225) 90%, #f1f1f1 100%);    background-size: 70%;    animation: shine-lines 3s infinite ease-out;     } @keyframes shine-lines {   0% {  background-position: -100px;   }   60%, 100% {  background-position: 650px;   } }  .container__months{   overflow: initial!important; }  .container__months .dropdown.bootstrap-select{   width: 100px!important;   position: relative;   left: 8px;   top: -1px; }  .container__months .dropdown-menu{   height: 150px; }  #user-accounts1 .sw-date-field .bootstrap-select>.dropdown-toggle:after {    display: none;     } #user-accounts1 .sw-date-field .filter-option {    height: 21px;     }  #user-accounts1 .sw-date-field .bootstrap-select .dropdown-toggle .filter-option-inner-inner {    text-align: center;     }  #user-accounts1 .sw-date-field{    display: flex!important;    justify-content: flex-start;     } #user-accounts1 .sw-date-field .dropdown-menu{    max-height: 200px;     } #user-accounts1 .sw-date-input {    border-color: transparent!important;    flex: 3;     } #user-accounts1 .sw-date-input:focus {    outline: none;     } #user-accounts1 .sw-time-input {    flex: 1;     } #user-accounts1 .sw-time-input.prevent-click {    pointer-events: none;    opacity: 0;    width: 0;     } #user-accounts1 .sw-date-input.input-alone {    width: 100%;     }  #user-accounts1 input::placeholder,     #user-accounts1 textarea::placeholder{        color: #adadad;      } #user-accounts1 select option{    color: #adadad;     } #user-accounts1 .sw-dropdown .bootstrap-select .dropdown-toggle .filter-option-inner-inner, #user-accounts1 .sw-multi-select .bootstrap-select .dropdown-toggle .filter-option-inner-inner{     min-height: 19px;   }  @keyframes onAutoFillStart {  from {/**/}  to {/**/} }  @keyframes onAutoFillCancel {  from {/**/}  to {/**/} } #toast-container{   bottom: 56px!important; }  div#toast-container> div.toast-error {   background-color: #FCEFEF;   background-image: url('https://softr-assets-eu-shared.s3.eu-central-1.amazonaws.com/studio/blocks/assets/toaster-close-icon.svg')!important;   color: #383B3D;   max-width: 400px!important;   width: 400px!important;   border-radius: 12px;   opacity: 1;   border: 0; } #toast-container> div {   border-right: 12px;   opacity: 1;   box-shadow: none!important; } #toast-container>.toast-error .toast-message{   max-width: 300px!important;   width: 300px!important; } #toast-container>.toast-error .toast-progress{   display: none; } #toast-container>.toast-error .toast-close-button{   color: #383B3D;   font-size: 15px;   font-weight: 500; } @media (max-width: 576px) {  #user-accounts1 #signup  {       padding: 25px 15px 25px;      }  #user-accounts1 .form  {       width: 310px;      } } 
.sw-text-color-000000 { color: #000000!important; } .sw-font-size-m { font-size: 1rem!important; } .sw-width-11xs { width: 2rem!important; } .sw-display-inline-block { display: inline-block!important; } .sw-font-family-default {  } .sw-font-weight-semibold { font-weight: 600!important; } .sw-letter-spacing-normal { letter-spacing: 0rem!important; } .sw-background-color-ffffff { background-color: #ffffff!important; } .sw-padding-top-2xl { padding-top: 6rem!important; } .sw-padding-bottom-2xl { padding-bottom: 6rem!important; } .sw-border-top-style-none { border-top-style: none!important; } .sw-border-top-width-xs { border-top-width: 1px!important; } .sw-border-top-color-000000 { border-top-color: #000000!important; } .sw-border-bottom-style-none { border-bottom-style: none!important; } .sw-border-bottom-width-xs { border-bottom-width: 1px!important; } .sw-border-bottom-color-000000 { border-bottom-color: #000000!important; } .sw-text-color-default {  } .sw-font-weight-default {  } .sw-padding-top-none { padding-top: 0rem!important; } .sw-padding-bottom-3xs { padding-bottom: 1.25rem!important; } .sw-display-block { display: block!important; } .sw-margin-top-3xs { margin-top: 1.25rem!important; } .sw-margin-bottom-3xs { margin-bottom: 1.25rem!important; } .sw-border-top-style-solid { border-top-style: solid!important; } .sw-border-top-color-cccccc { border-top-color: #cccccc!important; } .sw-width-4xs { width: 10rem!important; }  

        </style>

        <link href="https://fonts.softr-files.com/google/api/css?family=Nunito+Sans:600&display=swap" rel="stylesheet">
        <style>
            .made-with-softr {
              position: fixed;
              z-index: 9999999;
              left: 20px;
              bottom: 20px;
            }

            .made-with-softr a {
              width: 125px;
              font-style: normal;
              font-weight: 600;
              font-size: 14px;
              line-height: 19px;
              box-shadow: 0 0 4px rgb(0 0 0 / 15%);
              border-radius: 4px;
              z-index: 9999999;
              display: flex;
              justify-content: space-between;
              align-items: center;
              padding: 6px 8px;
              color: #1f2b3f;
              background: #ffffff;
              box-sizing: content-box;
              text-decoration: none;
              font-family: 'Nunito Sans', sans-serif;
            }
            .made-with-softr a .made-with {
              margin-left: 2px;
            }

            .made-with-softr a img {
                width: 16px;
            }

            .made-with-softr .softr-word {
              color: #3b85db;
            }

            .made-with-softr .dark-theme {
              color: #ffffff;
              background: #1f2b3f;
            }

            .made-with-softr .dark-theme .softr-word {
              color: #ffb30b;
            }
        </style>


    <!-- App Integrations -->
        
    <!-- End Integrations -->

        

        <script>window['application_context'] = {}; window['application_context']['policies'] ={"numberOfSupportedCollaborators":5,"numberOfSupportedDomains":1,"isSoftrBrandingVisible":true,"numberOfDatasourceRecordsPerTable":1000,"numberOfInternalUsers":5,"numberOfExternalUsers":100,"supportedNumberOfMembershipUsers":100,"hasSignInWithEmailCode":false,"hasSignInWithSMSCode":false,"hasGoogleAuthenticationSupport":true,"hasSamlAuthenticationSupport":false,"hasOpenIdAuthenticationSupport":false,"hasUserLastSeenSupport":false,"hasMapSupport":true,"hasTableSupport":true,"hasCalendarSupport":false,"hasInboxBlockSupport":false,"hasKanbanSupport":false,"hasChartsSupport":false,"hasOrgChartBlockSupport":false,"hasTimelineBlockSupport":false,"numberOfDaysApplicationHistory":7,"hasCustomCodeSupport":false,"hasEmbedBlockSupport":false,"hasTransferApplicationsAcrossWorkspace":false,"hasPwaSupport":true,"hasTransferOwnershipSupport":null,"hasEditAirtableRecordsSupport":false,"hasMultiGroupEditAirtableRecordsSupport":false}; </script>

    <!-- App Custom Header Code -->
        <style>
 .sw-font-size-5xl {
    font-size: 3rem;
  }
  .sw-font-size-4xl {
    font-size: 2.25rem;
  }
</style>
<script>
  document.addEventListener("DOMContentLoaded", () => {
    if($(window).width() < 768) {
       $('h1.sw-font-size-10xl').removeClass('sw-font-size-10xl').addClass('sw-font-size-5xl');
       $('h1.sw-font-size-9xl').removeClass('sw-font-size-9xl').addClass('sw-font-size-5xl');
       $('h1.sw-font-size-8xl').removeClass('sw-font-size-8xl').addClass('sw-font-size-5xl');
       $('h1.sw-font-size-7xl').removeClass('sw-font-size-7xl').addClass('sw-font-size-5xl');
       $('h1.sw-font-size-6xl').removeClass('sw-font-size-6xl').addClass('sw-font-size-4xl');
       $('h2.sw-font-size-10xl').removeClass('sw-font-size-10xl').addClass('sw-font-size-5xl');
       $('h2.sw-font-size-9xl').removeClass('sw-font-size-9xl').addClass('sw-font-size-5xl');
       $('h2.sw-font-size-8xl').removeClass('sw-font-size-8xl').addClass('sw-font-size-5xl');
       $('h2.sw-font-size-7xl').removeClass('sw-font-size-7xl').addClass('sw-font-size-5xl');
       $('h2.sw-font-size-6xl').removeClass('sw-font-size-6xl').addClass('sw-font-size-4xl');
       $('div.sw-font-size-10xl').removeClass('sw-font-size-10xl').addClass('sw-font-size-5xl');
       $('div.sw-font-size-9xl').removeClass('sw-font-size-9xl').addClass('sw-font-size-5xl');
       $('div.sw-font-size-8xl').removeClass('sw-font-size-8xl').addClass('sw-font-size-5xl');
       $('div.sw-font-size-7xl').removeClass('sw-font-size-7xl').addClass('sw-font-size-5xl');
       $('div.sw-font-size-6xl').removeClass('sw-font-size-6xl').addClass('sw-font-size-4xl');
       $('p.sw-font-size-10xl').removeClass('sw-font-size-10xl').addClass('sw-font-size-5xl');
       $('p.sw-font-size-9xl').removeClass('sw-font-size-9xl').addClass('sw-font-size-5xl');
       $('p.sw-font-size-8xl').removeClass('sw-font-size-8xl').addClass('sw-font-size-5xl');
       $('p.sw-font-size-7xl').removeClass('sw-font-size-7xl').addClass('sw-font-size-5xl');
       $('p.sw-font-size-6xl').removeClass('sw-font-size-6xl').addClass('sw-font-size-4xl');
       $('span.sw-font-size-10xl').removeClass('sw-font-size-10xl').addClass('sw-font-size-5xl');
       $('span.sw-font-size-9xl').removeClass('sw-font-size-9xl').addClass('sw-font-size-5xl');
       $('span.sw-font-size-8xl').removeClass('sw-font-size-8xl').addClass('sw-font-size-5xl');
       $('span.sw-font-size-7xl').removeClass('sw-font-size-7xl').addClass('sw-font-size-5xl');
       $('span.sw-font-size-6xl').removeClass('sw-font-size-6xl').addClass('sw-font-size-4xl');
    }
  });
</script>
    <!-- End App Custom Header Code -->

    <!-- Page Custom Header Code -->
        
    <!-- End Page Custom Header Code -->

        <script>window['is401Page'] = false; </script>
        

        <script>
            /** Image lineup on mobile **/
            document.addEventListener("DOMContentLoaded", function() {
                function changeImageDirectionsOnMobile() {

                    const classListSection = $('body>div>section')?.attr('class')?.split(/\s+/);
                    const textClassSection = classListSection?.find(cls => cls.startsWith('feature'));

                    const classListHeader = $('body>div>header')?.attr('class')?.split(/\s+/);
                    const textClassHeader = classListHeader?.find(cls => cls.startsWith('hero'));

                    /*If FEATURE block*/
                    if (textClassSection) {
                        findRowsWidthImageAndReverse(textClassSection)
                    }

                    /*If HERO block*/
                    if (textClassHeader) {
                        findRowsWidthImageAndReverse(textClassHeader)
                    }
                }

                function findRowsWidthImageAndReverse(textClass) {
                    const rowsWithImages = $('.' + textClass + ' .row.align-items-center').has('img').toArray();
                    const rowsWithLeftSideImages = rowsWithImages.filter(row => {
                        return $(row).children().first().children().first().prop("tagName") === 'IMG';
                    });


                    rowsWithLeftSideImages.forEach(row => {
                        if ($(window).width() <= 768) {
                            row.classList.add('flex-column-reverse')
                        }
                    });
                }

                if ($(window).width() <= 768) {
                    changeImageDirectionsOnMobile();
                }
            });

            /** BG Size on mobile **/
            document.addEventListener("DOMContentLoaded", function() {
                if($(window).width() <= 768) {
                    var element = $('section.sw-background-size-auto, header.sw-background-size-auto');
                    element.removeClass('sw-background-size-auto');
                    element.css('background-size', 'cover');

                    $('section.sw-background-attachment-fixed, header.sw-background-attachment-fixed').removeClass('sw-background-attachment-fixed');
                }
            });

            /** Disable zoom on mobile **/
            document.addEventListener("DOMContentLoaded", function() {
               if($(window).width() <= 768) {
                   $('input.sw-font-size-s').removeClass('sw-font-size-s');
                   $('textarea.sw-font-size-s').removeClass('sw-font-size-s');
                   $('select.sw-font-size-s').removeClass('sw-font-size-s');
               }
           });

        </script>
    </head>

    <body>

        <div data-appid="92c67a9d-f1be-49fe-ab2c-e331d53be0ab" data-pageId="720faf5c-c08f-4f86-8bf7-6c32bf7a82fd" data-workspaceid="5df1a107-e11b-41e0-a626-f9f28136a5c4" data-paymentplan="" class="content"><section id="faq1"    data-block-version="2.0.0" data-block-id="17507902-1ab4-4074-fef3-2110616dc1c3"    data-block-updated=""  class="faq1-17507902-1ab4-4074-fef3-2110616dc1c3 sw-background-color-ffffff sw-padding-top-2xl sw-padding-bottom-2xl sw-border-top-style-none sw-border-top-width-xs sw-border-top-color-000000 sw-border-bottom-style-none sw-border-bottom-width-xs sw-border-bottom-color-000000 ">  <div class="container">      <!-- Header -->      <div class="row">    <div class="col-12 text-center">     <h2  class="sw-font-size-4xl sw-text-color-default sw-font-family-default sw-font-weight-default sw-padding-top-none sw-padding-bottom-4xs sw-letter-spacing-normal sw-line-height-normal ">      Школьная столовая     </h2>    </div>   </div>       <!-- Subheader -->      <div class="row">    <div class="col-12 col-sm-10 offset-sm-1 text-center">     <p class="sw-font-size-xl sw-text-color-default sw-font-family-default sw-font-weight-default sw-padding-top-none sw-padding-bottom-3xs sw-letter-spacing-normal sw-line-height-normal ">      Кушайте вкусно!     </p>    </div>   </div>       <div class="row">    <div class="col-12 col-sm-10 offset-sm-1 text-center">     <div class="accordion sw-accordion-border" id="faq1-accordion">           </div>    </div>   </div>  </div> </section> <section id="faq2"    data-block-version="2.0.0" data-block-id="937ddf1b-10ae-4b23-a998-c7a57ab9c973"    data-block-updated=""  class="faq1-937ddf1b-10ae-4b23-a998-c7a57ab9c973 sw-background-color-ffffff sw-padding-top-2xl sw-padding-bottom-2xl sw-border-top-style-none sw-border-top-width-xs sw-border-top-color-000000 sw-border-bottom-style-none sw-border-bottom-width-xs sw-border-bottom-color-000000 ">  <div class="container">      <!-- Header -->      <div class="row">    <div class="col-12 text-center">     <h2  class="sw-font-size-4xl sw-text-color-default sw-font-family-default sw-font-weight-default sw-padding-top-none sw-padding-bottom-4xs sw-letter-spacing-normal sw-line-height-normal ">      Вопросы и ответы     </h2>    </div>   </div>       <!-- Subheader -->      <div class="row">    <div class="col-12 col-sm-10 offset-sm-1 text-center">     <p class="sw-font-size-xl sw-text-color-default sw-font-family-default sw-font-weight-default sw-padding-top-none sw-padding-bottom-3xs sw-letter-spacing-normal sw-line-height-normal ">      Есть вопрос? У нас есть ответы. Если остались вопросы свяжитесь с нами по электронной почте     </p>    </div>   </div>       <div class="row">    <div class="col-12 col-sm-10 offset-sm-1 text-center">     <div class="accordion sw-accordion-border" id="faq2-accordion">            <div class="mb-0 border-0 text-left">       <span data-toggle="collapse" href="#faq2-accordion-0" aria-expanded="false"           class="collapsed sw-font-size-m sw-text-color-default sw-font-family-default sw-font-weight-medium sw-background-color-f9fafb sw-letter-spacing-normal sw-padding-left-4xs sw-padding-top-4xs sw-padding-bottom-4xs sw-text-decoration-no-underline sw-display-block sw-border-bottom-style-solid sw-border-bottom-width-xs sw-border-bottom-color-f1f2f3 sw-cursor-pointer">         Можно ли есть несколько раз в день?        <span class="arrow"></span>       </span>              <div id="faq2-accordion-0" class="collapse" data-parent="#faq2-accordion">        <p class="sw-font-size-m sw-text-color-default sw-font-family-default sw-font-weight-normal sw-background-color-ffffff sw-line-height-normal sw-letter-spacing-normal sw-padding-left-4xs sw-padding-right-4xs sw-padding-top-4xs sw-margin-bottom-none sw-padding-bottom-4xs sw-border-bottom-style-solid sw-border-bottom-width-xs sw-border-bottom-color-f1f2f3">         Конечно! Мы всегда рады накормить детей        </p>       </div>      </div>            <div class="mb-0 border-0 text-left">       <span data-toggle="collapse" href="#faq2-accordion-1" aria-expanded="false"           class="collapsed sw-font-size-m sw-text-color-default sw-font-family-default sw-font-weight-medium sw-background-color-f9fafb sw-letter-spacing-normal sw-padding-left-4xs sw-padding-top-4xs sw-padding-bottom-4xs sw-text-decoration-no-underline sw-display-block sw-border-bottom-style-solid sw-border-bottom-width-xs sw-border-bottom-color-f1f2f3 sw-cursor-pointer">         Есть ли какие-то льготы?        <span class="arrow"></span>       </span>              <div id="faq2-accordion-1" class="collapse" data-parent="#faq2-accordion">        <p class="sw-font-size-m sw-text-color-default sw-font-family-default sw-font-weight-normal sw-background-color-ffffff sw-line-height-normal sw-letter-spacing-normal sw-padding-left-4xs sw-padding-right-4xs sw-padding-top-4xs sw-margin-bottom-none sw-padding-bottom-4xs sw-border-bottom-style-solid sw-border-bottom-width-xs sw-border-bottom-color-f1f2f3">         Да, для этого нужно оформить справку, подтверждающую ваше положение        </p>       </div>      </div>            <div class="mb-0 border-0 text-left">       <span data-toggle="collapse" href="#faq2-accordion-2" aria-expanded="false"           class="collapsed sw-font-size-m sw-text-color-default sw-font-family-default sw-font-weight-medium sw-background-color-f9fafb sw-letter-spacing-normal sw-padding-left-4xs sw-padding-top-4xs sw-padding-bottom-4xs sw-text-decoration-no-underline sw-display-block sw-border-bottom-style-solid sw-border-bottom-width-xs sw-border-bottom-color-f1f2f3 sw-cursor-pointer">         Есть бесплатное питание?        <span class="arrow"></span>       </span>              <div id="faq2-accordion-2" class="collapse" data-parent="#faq2-accordion">        <p class="sw-font-size-m sw-text-color-default sw-font-family-default sw-font-weight-normal sw-background-color-ffffff sw-line-height-normal sw-letter-spacing-normal sw-padding-left-4xs sw-padding-right-4xs sw-padding-top-4xs sw-margin-bottom-none sw-padding-bottom-4xs sw-border-bottom-style-solid sw-border-bottom-width-xs sw-border-bottom-color-f1f2f3">         Бесплатное питание только для начальных классов.        </p>       </div>      </div>           </div>    </div>   </div>  </div> </section> <script src="https://apis.google.com/js/api:client.js"></script> <section id="user-accounts1"    data-block-version="2.2.7" data-block-id="308d6a23-4087-44a1-b223-e1eccf9ad694"    data-block-updated=""    style=""    class="signup1-308d6a23-4087-44a1-b223-e1eccf9ad694 sw-background-color-ffffff sw-padding-top-2xl sw-padding-bottom-2xl sw-border-top-style-none sw-border-top-width-xs sw-border-top-color-000000 sw-border-bottom-style-none sw-border-bottom-width-xs sw-border-bottom-color-000000  sw-background-repeat-no-repeat sw-background-size-cover sw-background-position-center sw-background-attachment-scroll ">  <div class="container">   <div class="row align-items-center justify-content-center">    <div class="form sw-js-form" data-successUrl="/-">     <div id="signup"       class="col-12 text-left sw-background-color-ffffff sw-border-style-none sw-border-width-none sw-border-color-eaeced sw-border-radius-2xl sw-box-shadow-l ">       <!-- Logo -->                   <h2 class="text-center sw-font-size-2xl sw-text-color-default sw-font-family-default sw-font-weight-default sw-padding-top-none sw-padding-bottom-4xs sw-letter-spacing-normal sw-line-height-normal ">       Регистрация      </h2>            <!-- Error Message -->      <div class="error-message signup-error"></div>      <div class="error-message other-errors">         <img src="https://softr-assets-eu-shared.s3.eu-central-1.amazonaws.com/studio/blocks/assets/warning.svg">        Something went wrong, please try again.</div>      <div class="error-message required-errors">       <img src="https://softr-assets-eu-shared.s3.eu-central-1.amazonaws.com/studio/blocks/assets/warning.svg">        Please make sure there is no empty required fields.</div>              <div class="row align-items-center">                        <div class="col-12 text-center">          <input class="sw-background-color-FAFAFC hover:sw-background-color-FAFAFC sw-font-size-s sw-text-color-212121 sw-font-family-default sw-border-radius-l sw-padding-top-5xs sw-padding-bottom-5xs sw-margin-top-6xs sw-margin-bottom-6xs sw-border-style-solid sw-border-width-xs sw-border-color-F0F0F4 hover:sw-border-style-solid hover:sw-border-width-xs hover:sw-border-color-AEAEB5 sw-box-shadow-none sw-display-inline-block sw-padding-left-4xs sw-outline-none sw-width-full"              id="sw-form-capture-full_name-input"              type="text"              name="name"              placeholder="Полное имя"              required="true">         </div>               <div class="col-12 text-center">        <input class="sw-background-color-FAFAFC hover:sw-background-color-FAFAFC sw-font-size-s sw-text-color-212121 sw-font-family-default sw-border-radius-l sw-padding-top-5xs sw-padding-bottom-5xs sw-margin-top-6xs sw-margin-bottom-6xs sw-border-style-solid sw-border-width-xs sw-border-color-F0F0F4 hover:sw-border-style-solid hover:sw-border-width-xs hover:sw-border-color-AEAEB5 sw-box-shadow-none sw-display-inline-block sw-padding-left-4xs sw-outline-none sw-width-full"            id="sw-form-capture-email-input"            type="email"            name="email"            required="true"            placeholder="Электронная почта">       </div>       <div class="col-12">        <div class="col-12 m-0 p-0 text-center password position-relative d-inline-flex align-items-center sw-background-color-FAFAFC hover:sw-background-color-FAFAFC sw-font-size-s sw-text-color-212121 sw-font-family-default sw-border-radius-l sw-padding-top-5xs sw-padding-bottom-5xs sw-margin-top-6xs sw-margin-bottom-6xs sw-border-style-solid sw-border-width-xs sw-border-color-F0F0F4 hover:sw-border-style-solid hover:sw-border-width-xs hover:sw-border-color-AEAEB5 sw-box-shadow-none sw-padding-left-4xs sw-outline-none sw-width-full">         <input class=""             style="background: transparent "             id="sw-form-password-input"             type="password"             name="password"             required="true"             placeholder="Пароль">         <i class="fa fa-eye-slash show-password"></i>        </div>        <div class="col-12 m-0 p-0">         <div class="validation-message d-none">          <img src="https://softr-assets-eu-shared.s3.eu-central-1.amazonaws.com/studio/blocks/assets/warning.svg">           Password must contain at least 6 characters         </div>        </div>       </div>                     <div class="col-md-12 text-center d-flex flex-column">        <a data-element="button" id="sw-sign-up-submit-btn"           class="w-100 d-flex justify-content-center align-items-center sw-font-size-m sw-text-color-default sw-font-family-default sw-font-weight-default sw-border-radius-default sw-background-color-default hover:sw-background-color-default hover:sw-box-shadow-s sw-padding-left-xs sw-padding-right-xs sw-padding-top-5xs sw-padding-bottom-5xs sw-margin-top-none sw-margin-bottom-none sw-border-style-none sw-border-width-xs sw-border-color-000000 hover:sw-border-color-000000 sw-letter-spacing-normal sw-text-decoration-no-underline hover:sw-text-decoration-no-underline"           href="javascript:void(0);">         Регистрация         <div class="spinner-border sw-btn-spinner d-none text-light" role="status">          <span class="sr-only">Loading...</span>         </div>         <i class="fa fa-fw fa-check d-none" aria-hidden="true"></i>        </a>       </div>         <div class="col-md-12 text-center d-flex flex-column">        <a data-element="button" class="w-100 go-to-sign-in d-flex justify-content-center align-items-center sw-font-size-m sw-text-color-383B3D sw-font-family-default sw-font-weight-default sw-border-radius-default sw-background-color-ffffff hover:sw-background-color-ffffff hover:sw-box-shadow-none sw-padding-left-xs sw-padding-right-xs sw-padding-top-5xs sw-padding-bottom-5xs sw-margin-top-4xs sw-margin-bottom-none sw-border-style-solid sw-border-width-xs sw-border-color-F0F0F4 hover:sw-border-color-212121 sw-letter-spacing-normal sw-text-decoration-no-underline hover:sw-text-decoration-no-underline"           id="sw-go-to-sign-in-btn"           target=""           href="">         Вход        </a>       </div>       </div>      </div>    </div>    </div>   </div> </section> <footer id="home_footer1"    data-block-version="2.0.0" data-block-id="0a724bfe-641f-4633-9989-bb70f116e3ad"    data-block-updated=""  class="footer1-0a724bfe-641f-4633-9989-bb70f116e3ad sw-background-color-ffffff sw-padding-top-2xl sw-padding-bottom-2xl sw-border-top-style-none sw-border-top-width-xs sw-border-top-color-000000 sw-border-bottom-style-none sw-border-bottom-width-xs sw-border-bottom-color-000000 ">  <div class="container">   <div class="row align-items-center">        <div class=" col-12 pb-2">     <div class="nav justify-content-center justify-content-md-end">           </div>    </div>   </div>    <div class="row">    <div class="col-12">     <hr class="sw-margin-top-3xs sw-margin-bottom-3xs sw-border-top-style-solid sw-border-top-width-xs sw-border-top-color-cccccc ">    </div>   </div>    <div class="row">    <div class="col-7">     <small class="sw-font-size-m sw-text-color-default sw-font-family-default sw-font-weight-default sw-padding-top-none sw-padding-bottom-3xs sw-display-block">&copy; 2023 Права защищены Матерью всех школьных детей</small>    </div>     <div class="col-5">     <div class="text-right">           </div>    </div>   </div>    </div>  </div> </footer> </div>

        <script>

                function rgb2hex(orig) {
                    var rgb = orig.replace(/\s/g, "").match(/^rgba?\((\d+),(\d+),(\d+)/i);
                    return rgb && rgb.length === 4
                        ? "#" +
                        ("0" + parseInt(rgb[1], 10).toString(16)).slice(-2) +
                        ("0" + parseInt(rgb[2], 10).toString(16)).slice(-2) +
                        ("0" + parseInt(rgb[3], 10).toString(16)).slice(-2)
                        : orig;
                }

                function lightOrDark(color) {
                    // Variables for red, green, blue values
                    var r, g, b, hsp;

                    // Check the format of the color, HEX or RGB?
                    if (color.match(/^rgb/)) {
                        // If RGB --> store the red, green, blue values in separate variables
                        color = color.match(
                            /^rgba?\((\d+),\s*(\d+),\s*(\d+)(?:,\s*(\d+(?:\.\d+)?))?\)$/
                        );

                        r = color[1];
                        g = color[2];
                        b = color[3];
                    } else {
                        // If hex --> Convert it to RGB: http://gist.github.com/983661
                        color = +(
                            "0x" + color.slice(1).replace(color.length < 5 && /./g, "$&$&")
                        );

                        r = color >> 16;
                        g = (color >> 8) & 255;
                        b = color & 255;
                    }

                    // HSP (Highly Sensitive Poo) equation from http://alienryderflex.com/hsp.html
                    hsp = Math.sqrt(0.299 * (r * r) + 0.587 * (g * g) + 0.114 * (b * b));

                    // Using the HSP value, determine whether the color is light or dark
                    if (hsp > 127.5) {
                        return "light";
                    } else {
                        return "dark";
                    }
                }

        </script>

            
            

        <!-- Scripts -->
        <script src="https://assets.softr-files.com/libs/jquery/3.4.1/jquery.min.js"></script>
        <script src="https://assets.softr-files.com/libs/popper.js/1.14.7/umd/popper.min.js"></script>
        <script src="https://assets.softr-files.com/libs/bootstrap/4.3.1/js/bootstrap.min.js"></script>
        <script src="https://assets.softr-files.com/libs/micromodal/0.4.10/micromodal.min.js"></script>

        <script>
            /** Bugfix on multiple ?recordId= issue **/
            setInterval(function() {
                $('section a').each(function() {
                    const href = $(this).attr('href');
                    if(href && href.includes('?recordId=')) {
                        const countOfRecords = (href.match(/\?recordId=/g) || []).length;
                        if(countOfRecords > 1) {
                            const index = href.lastIndexOf('?recordId=');
                            const cleanedHref = href.substring(0, index);
                            $(this).attr('href', cleanedHref);
                        }
                    }
                });
            }, 1000);
        </script>

        <script type="text/javascript">
            if(window.jQuery && window.jQuery.ajaxSetup) {
                window.jQuery.ajaxSetup({
                    beforeSend: function(xhr, settings) {
                        if(settings && settings.url && (
                        settings.url.includes('/integrations/airtable/')
                        || settings.url.includes('/v1/applications/92c67a9d-f1be-49fe-ab2c-e331d53be0ab')
                        || settings.url.includes('/v1/comments')
                        || settings.url.includes('/forms/form-to-email'))
                        ){
                            xhr.setRequestHeader('softr-page-id', '720faf5c-c08f-4f86-8bf7-6c32bf7a82fd');
                        }
                    }
                });
            }

            window['faq1'] = {}; ; (function () {    var bgColor = window.getComputedStyle(document.querySelector('#faq1-accordion span'), null).getPropertyValue('background-color');  if(lightOrDark(bgColor) === 'dark') {   $('#faq1 .arrow').css('border-left', '2px solid #ffffff');   $('#faq1 .arrow').css('border-top', '2px solid #ffffff');  }   function lightOrDark(color) {    /* Variables for red, green, blue values */   var r, g, b, hsp;    /* Check the format of the color, HEX or RGB? */   if (color.match(/^rgb/)) {     /* If HEX --> store the red, green, blue values in separate variables */    color = color.match(/^rgba?\((\d+),\s*(\d+),\s*(\d+)(?:,\s*(\d+(?:\.\d+)?))?\)$/);     r = color[1];    g = color[2];    b = color[3];   }   else {     /* If RGB --> Convert it to HEX: http://gist.github.com/983661 */    color = +("0x" + color.slice(1).replace(     color.length < 5 && /./g, '$&$&'));     r = color >> 16;    g = color >> 8 & 255;    b = color & 255;   }    /* HSP (Highly Sensitive Poo) equation from http://alienryderflex.com/hsp.html */   hsp = Math.sqrt(    0.299 * (r * r) +    0.587 * (g * g) +    0.114 * (b * b)   );    /* Using the HSP value, determine whether the color is light or dark */   if (hsp > 127.5) {     return 'light';   }   else {     return 'dark';   }  }  })();  window['faq2'] = {}; ; (function () {    var bgColor = window.getComputedStyle(document.querySelector('#faq2-accordion span'), null).getPropertyValue('background-color');  if(lightOrDark(bgColor) === 'dark') {   $('#faq2 .arrow').css('border-left', '2px solid #ffffff');   $('#faq2 .arrow').css('border-top', '2px solid #ffffff');  }   function lightOrDark(color) {    /* Variables for red, green, blue values */   var r, g, b, hsp;    /* Check the format of the color, HEX or RGB? */   if (color.match(/^rgb/)) {     /* If HEX --> store the red, green, blue values in separate variables */    color = color.match(/^rgba?\((\d+),\s*(\d+),\s*(\d+)(?:,\s*(\d+(?:\.\d+)?))?\)$/);     r = color[1];    g = color[2];    b = color[3];   }   else {     /* If RGB --> Convert it to HEX: http://gist.github.com/983661 */    color = +("0x" + color.slice(1).replace(     color.length < 5 && /./g, '$&$&'));     r = color >> 16;    g = color >> 8 & 255;    b = color & 255;   }    /* HSP (Highly Sensitive Poo) equation from http://alienryderflex.com/hsp.html */   hsp = Math.sqrt(    0.299 * (r * r) +    0.587 * (g * g) +    0.114 * (b * b)   );    /* Using the HSP value, determine whether the color is light or dark */   if (hsp > 127.5) {     return 'light';   }   else {     return 'dark';   }  }  })();  window['user-accounts1'] = {}; ;(function () {   const emailInputSelector = '#user-accounts1 #sw-form-capture-email-input';   const nameInputSelector = '#user-accounts1 #sw-form-capture-full_name-input';   const passwordInputSelector = '#user-accounts1 #sw-form-password-input';   const termsInputSelector = '#user-accounts1 #user-accounts1-sw-form-terms-input';   const passwordBox = '#user-accounts1 .password';   const passwordValidationMessage = '#user-accounts1 .validation-message';   const submitButtonSelector = '#user-accounts1 #sw-sign-up-submit-btn';   const formElemenetsSelector = '#user-accounts1 .sw-form-capture-element';   const formDropdownWrapperElemenetsSelector = '#user-accounts1 div.bootstrap-select';   const dateTimeWrapperElemenetsSelector = '#user-accounts1 div.sw-date-field';   const formFileElemenetsSelector = '#user-accounts1 .sw-js-file-upload';   const checkboxElemenetsSelector = '#user-accounts1 span.checkmark';   const dragAreaSelector = '#user-accounts1 .drag-file-area';   const browseButtonSelector = '#user-accounts1 .sw-js-browse-link';   let pickers = [];   let filesToUpload = {};   let uploadedFileUrls = {};    const initGoogleSignUpButton = function () {  gapi.load('auth2', function () {    auth2 = gapi.auth2.init({   client_id: window.google_client_id,   cookiepolicy: 'single_host_origin',   fetch_basic_profile: true,   scope: 'profile email',   plugin_name: 'softr_gpl_fix'    });    attachSignUpButton(document.getElementById('sw-go-to-google-sign-up-btn'));  });   };    function attachSignUpButton(buttonElement) {  auth2.attachClickHandler(    buttonElement,    {},    function (googleUser) {   var googleUserData = {     email: googleUser.getBasicProfile().getEmail(),     name: googleUser.getBasicProfile().getName(),     token: googleUser.getAuthResponse().id_token,     provider: googleUser.getAuthResponse().idpId   };   makeGoogleSignUpRequest(googleUserData, handleGoogleSignUpSuccess, handleGoogleSignUpFailure);    },    function (error) {   handleGoogleSignUpFailure(error);    });   }    const appId = $('body > div.content').attr('data-appid');   const successUrl = $('#user-accounts1 .sw-js-form').attr('data-successUrl');    const showPassword = '#user-accounts1 .show-password';    const googleSingUpErrorMessage = '#user-accounts1 .google-signup-error';   const errorMessage1 = '#user-accounts1 .signup-error';   const errorMessage2 = '#user-accounts1 .other-errors';   const requiredError = '#user-accounts1 .required-errors';    appendStyle('https://cdn.jsdelivr.net/npm/bootstrap-select@1.13.14/dist/css/bootstrap-select.min.css');   appendScript('https://cdn.jsdelivr.net/npm/bootstrap-select@1.13.14/dist/js/bootstrap-select.min.js', initSelectPickers);    appendStyle('https://cdnjs.cloudflare.com/ajax/libs/toastr.js/2.1.4/toastr.min.css');   appendScript('https://cdnjs.cloudflare.com/ajax/libs/toastr.js/2.1.4/toastr.min.js');    appendStyle('https://cdn.jsdelivr.net/npm/litepicker@2.0.11/dist/css/litepicker.css');   appendScript('https://cdn.jsdelivr.net/npm/litepicker@2.0.11/dist/litepicker.js', loadLitepickerMobileFriendlyPlugin);    function loadLitepickerMobileFriendlyPlugin() {  appendScript('https://cdn.jsdelivr.net/npm/litepicker@2.0.11/dist/plugins/mobilefriendly.js', initDatePicker);   }    initSelectPickers();   initDatePicker();    function initSelectPickers() {  if ($('#user-accounts1 select').selectpicker) {    $('#user-accounts1 select').selectpicker();    $('#user-accounts1 select').removeClass('d-none');    $('#user-accounts1 select').addClass('d-block');  } else {    const existCondition = setInterval(function () {   if ($('#user-accounts1 select').selectpicker) {     $('#user-accounts1 select').selectpicker();     $('#user-accounts1 select').removeClass('d-none');     $('#user-accounts1 select').addClass('d-block');     clearInterval(existCondition);   }    }, 100);  }   }    function initDatePicker() {  if (pickers.length > 0) {    return;  }  if (window['Litepicker']) {    setupDatePicker();    setupDateTimePicker();  } else {    let existCondition = setInterval(() => {   if (window['Litepicker']) {     if (pickers.length > 0) {    return;     }     setupDatePicker();     setupDateTimePicker();     clearInterval(existCondition);   }    }, 100);  }   }    function setupDatePicker() {  $("input[data-type='date']").each(function () {    const element = $(this).get()[0];    const picker = new Litepicker({   element: element,   plugins: ['mobilefriendly'],   format: 'MMMM D YYYY',   dropdowns: {minYear: 1930, maxYear: null, months: false, years: true},   startDate: '',   setup: (pkr) => {     pkr.on('selected', (date) => {    $(element).attr('data-date-formatted-value', date.format('YYYY-MM-DD'));     });     pkr.on('change:year', (date, calendarIdx) => {    $('select.month-item-year').selectpicker();    let activeDate = $(element).attr('data-date-formatted-value').split('-');    activeDate[0] = date.getFullYear();    pkr.setDate(activeDate.join('-'));    pkr.hide();    pkr.show();     });     pkr.on('change:month', (date, calendarIdx) => {    $('select.month-item-year').selectpicker();     });     pkr.on('show', (el) => {    $('select.month-item-year').selectpicker();     });   }    });    pickers.push(picker);  });   }    function setupDateTimePicker() {  $("input[data-type='dateTime']").each(function () {    const element = $(this).get()[0];    const picker = new Litepicker({   element: element,   plugins: ['mobilefriendly'],   format: 'MMMM D YYYY',   dropdowns: {minYear: 1930, maxYear: null, months: false, years: true},   startDate: '',   setup: (pkr) => {     pkr.on('selected', (date) => {    const selectElement = $(element)[0].nextElementSibling.querySelector('select');    $(element)[0].nextElementSibling.classList.remove('prevent-click');    let selectedTime = selectElement.getAttribute('data-time-formatted-value');    if (!selectedTime) {      selectElement.value = '00:00';      selectedTime = '00:00';      $('select[data-type="time"]').trigger('change');    }    const selectedDate = date.format('YYYY-MM-DD');    $(element).attr('data-datetime-formatted-value', selectedDate + ' ' + selectedTime);    removeSelectDefaultPlaceholder();     });     pkr.on('change:year', (date, calendarIdx) => {    $('select.month-item-year').selectpicker();    let activeDate = $(element).attr('data-datetime-formatted-value').split('-');    activeDate[0] = date.getFullYear();    pkr.setDate(activeDate.join('-'));    pkr.hide();    pkr.show();     });     pkr.on('change:month', (date, calendarIdx) => {    $('select.month-item-year').selectpicker();     });     pkr.on('show', (el) => {    $('select.month-item-year').selectpicker();     });   }    });    pickers.push(picker);  });   $("select[data-type='time']").change(function () {    const element = $(this).get()[0];    const dateInputElement = $(element)[0].parentElement.previousElementSibling;    const selectedTime = $(this).val();    $(element).attr('data-time-formatted-value', selectedTime);    let selectedDate = dateInputElement.getAttribute('data-datetime-formatted-value');    if (selectedDate) {   selectedDate = selectedDate.split(' ')[0];    }    dateInputElement.setAttribute('data-datetime-formatted-value', selectedDate + ' ' + selectedTime);    removeSelectDefaultPlaceholder();  });   console.log('Setup time picker');  setTimeout(() => removeSelectDefaultPlaceholder(), 100);   }    function removeSelectDefaultPlaceholder() {  console.log('REMOVE PLACEHOLDER');  setTimeout(() => {    [...document.querySelectorAll('[class*="filter-option-inner-inner"]')]   .forEach(txt => {     if (txt && txt.innerHTML.includes('Nothing selected')) {    txt.innerHTML = ''     }   });  });   }    $('#user-accounts1 input').keyup((evt) => {  if (evt.which === 13) {    evt.preventDefault();    $(submitButtonSelector).click();  }   });    function isEmail(email) {  const emailReg = /^(([^<>()[\]\\.,;:\s@\"]+(\.[^<>()[\]\\.,;:\s@\"]+)*)|(\".+\"))@((\[[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\])|(([a-zA-Z\-0-9]+\.)+[a-zA-Z]{2,}))$/;  return email && emailReg.test(email);   }    function validURL(str) {  let pattern = new RegExp('^(https?:\\/\\/)?'+    '((([a-z\\d]([a-z\\d-]*[a-z\\d])*)\\.)+[a-z]{2,}|'+    '((\\d{1,3}\\.){3}\\d{1,3}))'+    '(\\:\\d+)?(\\/[-a-z\\d%_.~+]*)*'+    '(\\?[;&a-z\\d%_.~+=-]*)?'+    '(\\#[-a-z\\d_]*)?$','i');  return !!pattern.test(str);   }    function isEmpty(value) {  return !value;   }    function handleSuccess(data) {  setCookie('jwtToken', data.jwt, 90);  setTimeout(function () {    /* when page includes login and after login it remains in same page */    /* when sign in block in 401 page, after login reload the page as 401 page's url is same */    if (window.location.pathname === successUrl || window.is401Page) {   window.location.reload();    } else {   window.location.href = successUrl;    }    $(emailInputSelector).val('');    $(nameInputSelector).val('');    $(passwordInputSelector).val('');  }, 100);   }    function handleGoogleSignUpSuccess(data) {  setCookie('jwtToken', data.jwt, 90);  setTimeout(function () {    /* when page includes login and after login it remains in same page */    /* when sign in block in 401 page, after login reload the page as 401 page's url is same */    if (window.location.pathname === successUrl || window.is401Page) {   window.location.reload();    } else {   window.location.href = successUrl;    }  }, 100);   }    function handleFailure(data) {  $(submitButtonSelector + ' .sw-btn-spinner').addClass('d-none');   if (data && data.responseJSON && data.responseJSON.message) {    if(data.responseJSON.code === 'exceeds_limit') {   showErrorToastr(data.responseJSON.message);   return;    }  }   $(nameInputSelector).addClass('sw-input-invalid');  $(emailInputSelector).addClass('sw-input-invalid');  $(termsInputSelector).addClass('sw-invalid-checkbox');  $(passwordBox).addClass('sw-input-invalid');   $(formElemenetsSelector).each(function () {    $(this).addClass('sw-input-invalid');  });  $(formFileElemenetsSelector).each(function () {    $(this).addClass('sw-input-invalid');  });  $(formDropdownWrapperElemenetsSelector).each(function () {    $(this).addClass('sw-input-invalid');  });  $(dateTimeWrapperElemenetsSelector).each(function () {    $(this).addClass('sw-input-invalid');  });  $(checkboxElemenetsSelector).each(function (i, element) {    element.classList.add('sw-input-invalid');  });   if (data.responseJSON.code === 'email_already_exists' || data.responseJSON.code === 'domain_restricted') {    const error = `    <img src="https://softr-assets-eu-shared.s3.eu-central-1.amazonaws.com/studio/blocks/assets/warning.svg">    ${data.responseJSON.message}    `;     $(errorMessage1).html(error);    $(errorMessage1).addClass('d-flex');    $(errorMessage2).removeClass('d-block');  } else {    $(errorMessage1).removeClass('d-block');    $(errorMessage2).addClass('d-flex');  }    }    function handleGoogleSignUpFailure(data) {  if (data.error && data.error.indexOf('popup_closed_by_user') !== -1) {    return;  }   if (data && data.responseJSON && data.responseJSON.message) {    showErrorToastr(data.responseJSON.message);    if(data.responseJSON.code === 'exceeds_limit') {   return;    }  }   /* Softr errors */  if (data.status === 400 && data.responseJSON && data.responseJSON.message) {    $(googleSingUpErrorMessage).text(data.responseJSON.message);  }  $(googleSingUpErrorMessage).addClass('d-flex');   }    function isValidPassword(pwd) {  if (!pwd) {    return null;  }  return pwd.length >= 6;   }    function makeSignupRequest(data, successCallback, errorCallback) {  clearToasterError();  const apiBaseUrl = getApiBaseUrl();  const url = apiBaseUrl + '/v1/applications/' + appId + '/users';  $.ajax({    url: url,    type: 'POST',    data: JSON.stringify(data),    contentType: 'application/json; charset=utf-8',    dataType: 'json',    success: function (data) {   console.log(data);   successCallback(data);    },    error: function (error) {   console.log(error);   errorCallback(error);    }  });   }    function makeSigninRequest(email, password, successCallback, errorCallback) {  clearToasterError();  const apiBaseUrl = getApiBaseUrl();  const url = apiBaseUrl + '/v1/applications/' + appId + '/users/tokens';  $.ajax({    url: url,    type: 'POST',    data: JSON.stringify({email: email, password: password}),    contentType: 'application/json; charset=utf-8',    dataType: 'json',    success: function (data) {   console.log(data);   successCallback(data);    },    error: function (error) {   console.log(error);   errorCallback(error);    }  });   }    function makeGoogleSignUpRequest(googleUserData, successCallback, errorCallback) {  clearToasterError();  const apiBaseUrl = getApiBaseUrl();  const url = apiBaseUrl + '/v1/applications/' + appId + '/users/social';  $.ajax({    url: url,    type: 'POST',    data: JSON.stringify({   credentials: {     email: googleUserData.email,     token: googleUserData.token   },   full_name: googleUserData.name,   provider: googleUserData.provider    }),    contentType: 'application/json; charset=utf-8',    dataType: 'json',    success: function (data) {   console.log(data);   successCallback(data);    },    error: function (error) {   console.log(error);   errorCallback(error);    }  });   }    $(submitButtonSelector).click(function (e) {  e.preventDefault();   let fullName = "";  const fullNameInput = $(nameInputSelector);  /*full name can be disabled*/  if (fullNameInput.length > 0) {    fullName = $(nameInputSelector).val().trim();  }   const email = $(emailInputSelector).val().trim();  const password = $(passwordInputSelector).val().trim();  const terms = $(termsInputSelector).is(':checked');    /* validate the input */  if ($(nameInputSelector).length > 0) {    $(nameInputSelector).removeClass('sw-input-invalid');    if (isEmpty(fullName)) {   $(nameInputSelector).addClass('sw-input-invalid');    }  }   /* validate the input */  $(emailInputSelector).removeClass('sw-input-invalid');  if (!isEmail(email)) {    $(emailInputSelector).addClass('sw-input-invalid');  }    /* validate the input */  $(passwordBox).removeClass('sw-input-invalid');  $(passwordValidationMessage).removeClass('d-block');  if (!isValidPassword(password)) {    $(passwordBox).addClass('sw-input-invalid');    $(passwordValidationMessage).addClass('d-block');  }   /* validate the terms checkbox */  if ($(termsInputSelector).length > 0) {    $(termsInputSelector).removeClass('sw-invalid-checkbox');    if (!terms) {   $(termsInputSelector).addClass('sw-invalid-checkbox');    }  }   $(requiredError).addClass('d-block');    let isFormValid = true;   $(formElemenetsSelector).each(function () {     $(this).removeClass('sw-input-invalid');    if ($(this).attr('data-required') === 'true' && !$(this).val()) {   isFormValid = false;   $(this).addClass('sw-input-invalid');    }    if ($(this).attr('data-type') === 'email') {   if ($(this).attr('data-required') === 'true') {     if (!isEmail($(this).val().trim())) {    isFormValid = false;    $(this).addClass('sw-input-invalid');     }   } else {     if ($(this).val() && !isEmail($(this).val().trim())) {    isFormValid = false;    $(this).addClass('sw-input-invalid');     }   }    }     if ($(this).attr('data-type') === 'url') {   if ($(this).attr('data-required') === 'true') {     if (!validURL($(this).val().trim())) {    isFormValid = false;    $(this).addClass('sw-input-invalid');     }   } else {     if ($(this).val() && !validURL($(this).val().trim())) {    isFormValid = false;    $(this).addClass('sw-input-invalid');     }   }     }  });     $(formDropdownWrapperElemenetsSelector).each(function () {    const select = $(this).find('select');    $(this).removeClass('sw-input-invalid');     if (select.attr('data-required') === 'true') {    if (!$(this).find('select').val()) {     isFormValid = false;     $(this).addClass('sw-input-invalid');   }    if (select.attr('data-type') === 'multi_select' &&     !select.val().length) {     isFormValid = false;     $(this).addClass('sw-input-invalid');   }     }   });   $(dateTimeWrapperElemenetsSelector).each(function () {    $(this).removeClass('sw-input-invalid');    if ($(this).find('input').attr('data-required') === 'true' && !$(this).find('input').val()) {   isFormValid = false;   $(this).addClass('sw-input-invalid');    }  });   $(checkboxElemenetsSelector).each(function (i, element) {    element.classList.remove('sw-input-invalid');    if (element.previousElementSibling.getAttribute('data-required') === 'true' && !element.previousElementSibling.checked) {   isFormValid = false;   element.classList.add('sw-input-invalid');    }  });   $(formFileElemenetsSelector).each(function () {    $(this).removeClass('sw-input-invalid');    const key = $(this).attr('data-name');    if ($(this).attr('data-required') === 'true' && (uploadedFileUrls[key] === undefined || uploadedFileUrls[key] === null || uploadedFileUrls[key].length === 0)) {   isFormValid = false;   $(this).addClass('sw-input-invalid');    }  });   if (!isEmail(email) ||    ($(nameInputSelector).length > 0 && isEmpty(fullName)) ||    !isValidPassword(password) ||    ($(termsInputSelector).length > 0 && !terms)) {    return;  }   if (!isFormValid) {    return;  }   $(requiredError).removeClass('d-block');   $(submitButtonSelector + ' .sw-btn-spinner').removeClass('d-none');   const attributes = {};   $(formElemenetsSelector).not('div.bootstrap-select').each(function (index) {    let name = $(this).attr('name');    const elementId = $(this).attr('id');    const dataType = $(this).attr('data-type');    const dataMappedTo = $(this).attr('data-mappedTo');    const inputValue = $(this).val();     let mappedField = '';     if (dataMappedTo) {   mappedField = dataMappedTo;    } else if (name) {   mappedField = name;    } else {   mappedField = 'FIELD_' + index;    }     if (dataType === 'hidden') {   attributes[mappedField] = setHiddenFieldValue(inputValue);    } else if (dataType === 'date') {   attributes[mappedField] = $(this).attr('data-date-formatted-value');    } else if (dataType === 'dateTime') {   attributes[mappedField] = $(this).attr('data-datetime-formatted-value');    } else if (dataType === 'file') {     } else if (dataType === 'password') {   attributes[name] = inputValue.toString();    } else {   attributes[mappedField] = inputValue.toString();   /*do not send full name in attributes, if full name is not mapped*/   if (elementId === 'sw-form-capture-full_name-input' || elementId === 'sw-form-capture-email-input') {     delete attributes['full_name'];     delete attributes[mappedField];   }    }  });   $('#user-accounts1 .sw-form-capture-element-checkbox').each(function (index) {    let name = $(this).attr('name');    let dataMappedTo = $(this).attr('data-mappedTo');     const inputValue = $(this).is(':checked');     let mappedField = '';    if (dataMappedTo) {   mappedField = dataMappedTo;    } else if (name) {   mappedField = name;    } else {   mappedField = 'FIELD_' + index;    }    attributes[mappedField] = inputValue;  });   delete attributes['SW-TIME-FIELD'];  delete attributes['password'];   /* File upload urls */  if (JSON.stringify(uploadedFileUrls) !== '{}') {    for (let key in uploadedFileUrls) {   uploadedFileUrls[key].forEach(function (file) {     attributes[key] = file.url;   });    }  }   let formData = {    full_name: fullName,    credentials: {   email,   password    },    is_terms_supported: $(termsInputSelector).length > 0,    is_terms_accepted: ($(termsInputSelector).length > 0 && terms)  };   formData['attributes'] = attributes;  console.log('formData', formData);  makeSignupRequest(formData, function () {    makeSigninRequest(email, password, handleSuccess, handleFailure);  }, handleFailure);    });    $(browseButtonSelector).click(function (e) {  e.preventDefault();  const key = $(e.target).parents('.sw-js-file-upload').attr('data-name');  $('#user-accounts1 div[data-name="' + key + '"] .sw-js-file-input').click();   });    $(dragAreaSelector).on('dragover', () => {  return false;   });    $(dragAreaSelector).on('dragleave', () => {  return false;   });    $(dragAreaSelector).on('dragend', () => {  return false;   });    $(dragAreaSelector).on('drop', (e) => {  e.preventDefault();  const key = $(e.target).parents('.sw-js-file-upload').attr('data-name');  parseFiles(e.originalEvent.dataTransfer.files, key);  uploadFiles(e.originalEvent.dataTransfer.files, key);   });    $(formFileElemenetsSelector).on('change', (e) => {  e.preventDefault();  const key = $(e.target).parents('.sw-js-file-upload').attr('data-name');  parseFiles($('#user-accounts1 div[data-name="' + key + '"] .sw-js-file-input').prop('files'), key);  uploadFiles($('#user-accounts1 div[data-name="' + key + '"] .sw-js-file-input').prop('files'), key);   });    $(showPassword).click(function () {  let password = $('#user-accounts1 #sw-form-password-input');  if (password.attr('type') === 'password') {    password.attr('type', 'text');    $(this).addClass('active fa-eye');    $(this).removeClass('fa-eye-slash');  } else {    password.attr('type', 'password');    $(this).removeClass('active fa-eye');    $(this).addClass('fa-eye-slash');  }   });    function uploadFiles(files, key) {  for (let file of files) {    const formData = new FormData();    formData.append("file", file);    $('#user-accounts1 li[data-name="' + normalizeFileName(file.name) + '"] span.sw-js-progressbar').addClass('progressbar');    $('#user-accounts1 li[data-name="' + normalizeFileName(file.name) + '"] span.sw-js-progressbar').addClass('blink');     $.ajax({   type: "POST",   url: getFileUploadUrl(appId),   xhr: function () {     var myXhr = $.ajaxSettings.xhr();     return myXhr;   },   success: function (data) {     console.log(data);     if (uploadedFileUrls[key] === undefined || uploadedFileUrls[key] === null) {    uploadedFileUrls[key] = [];     }     uploadedFileUrls[key].push({    name: normalizeFileName(file.name),    url: data     });     $('#user-accounts1 li[data-name="' + normalizeFileName(file.name) + '"] span.progressbar').removeClass('blink');   },   error: function (error) {      console.log(error);   },   async: true,   data: formData,   cache: false,   contentType: false,   processData: false,   timeout: 60000    });  }   }    function parseFiles(files, key) {  let tempFiles = [];   for (let file of files) {    tempFiles.push(file);  }  if (filesToUpload[key] === undefined || filesToUpload[key] === null) {    filesToUpload[key] = [];  }  filesToUpload[key] = tempFiles.concat(filesToUpload[key]);  rerenderFilesList(key);   }    function rerenderFilesList(key) {  if (filesToUpload[key].length === 0) {    $('#user-accounts1 div[data-name="' + key + '"] .sw-js-file-list').hide();  } else {    $('#user-accounts1 div[data-name="' + key + '"] .sw-js-file-list').show();  }  $('#user-accounts1 div[data-name="' + key + '"] .sw-js-file-list').css('padding', '10px 0');  const ul = document.createElement('ul');  filesToUpload[key].forEach(file => {    const li = document.createElement('li');    li.setAttribute('data-name', normalizeFileName(file.name));    const progressBar = document.createElement('span');    const deleteFile = document.createElement("span");    const fileName = document.createElement("span");    const div = document.createElement("div");    deleteFile.className = "delete";    deleteFile.innerHTML = "&#x2715;";    progressBar.className = "sw-js-progressbar progressbar";    fileName.innerText = file.name;    div.append(fileName);    div.append(deleteFile);    li.append(div);    li.append(progressBar);    ul.appendChild(li);  });  $('#user-accounts1 div[data-name="' + key + '"] .sw-js-file-list').html(ul.innerHTML);   $('#user-accounts1 div[data-name="' + key + '"] .sw-js-file-list li span.delete').click(e => {    const fileName = e.target.previousElementSibling.innerHTML;    const index = filesToUpload[key].findIndex(file => file.name === fileName);    filesToUpload[key].splice(index, 1);     if (uploadedFileUrls[key]) {   const urlIndex = uploadedFileUrls[key].findIndex(url => url.name === normalizeFileName(fileName));   uploadedFileUrls[key].splice(urlIndex, 1);    }     rerenderFilesList(key);    $('#user-accounts1 div[data-name="' + key + '"] .sw-js-file-input').val('');  });   }    function normalizeFileName(name) {  var nameClone = new String(name);  return nameClone.replace(/[^0-9a-zA-Z_-]/gi, '');   }    function getFileUploadUrl(applicationId) {  if (window.location.href.startsWith('file:///')) {    return 'http://localhost:8081/v1/applications/' + applicationId + '/upload';  }  if (window.location.href.startsWith('http://localhost:')) {    return 'http://localhost:8081/v1/applications/' + applicationId + '/upload';  }  if (window.location.href.includes('preview.staging')) {    return 'https://' + window.location.hostname + '/v1/applications/' + applicationId + '/upload';  }  if (window.location.href.includes('preview.softr.io/')) {    return 'https://' + window.location.hostname + '/v1/applications/' + applicationId + '/upload';  } else {    return 'https://' + window.location.hostname + '/v1/applications/' + applicationId + '/upload';  }   }    /* 'or' separator bg color*/   const formClassList = [...document.querySelector('#user-accounts1 #signup').classList];   const formBgColor = formClassList.find((clazz) => clazz.startsWith('sw-background-color-'));   const [formColorCode] = formBgColor.split('-').reverse();   $('.textInSeparator').css({  backgroundColor: `#${formColorCode}`   });    /* 'term' 'privacy'  color*/   if ($(termsInputSelector).length > 0) {  const classList = [...document.querySelector('#user-accounts1 .terms label').classList];  const termColor = classList.find((clazz) => clazz.startsWith('sw-text-color-'));  const [colorCode] = termColor.split('-').reverse();  $('.terms-link').css({    color: `#${colorCode}`  });   }    function getApiBaseUrl() {  if (window.location.href.startsWith('file:///') ||    window.location.href.startsWith('http://localhost:')) {    return 'http://localhost:8081';  } else {    return 'https://' + window.location.hostname;  }   }    function setCookie(name, value, days) {  var date = new Date();  date.setTime(date.getTime() + (days * 24 * 60 * 60 * 1000));  var expires = "expires=" + date.toUTCString();  document.cookie = name + "=" + value + ";" + expires + ";path=/;" + 'SameSite=None; Secure';   }    function setHiddenFieldValue(inputValue) {  let hiddenFieldValue = inputValue.trim();  switch (true) {    case hiddenFieldValue === '{PAGE}': {   hiddenFieldValue = getCurrentPageUrl();   break;    }    case hiddenFieldValue.startsWith('{URL_PARAM:'): {   const afterDots = inputValue.split(':')[1];   const urlParams = afterDots.split('}')[0];   hiddenFieldValue = getUrlParam(urlParams);   break;    }  }  return hiddenFieldValue;   }    function getCurrentPageUrl() {  return location.href;   }    function getUrlParam(name) {  const url = new URL(window.location.href);  let param;  for (var key of url.searchParams.keys()) {    if (key.toLowerCase() === name.toLowerCase()) {   param = url.searchParams.get(name);   break;    }  }  return param;   }    function checkboxSizeCalculation() {  const checkboxes = $('#user-accounts1 .checkmark');  const smallSizes = ['3xs', '2xs', 'xs', 's', 'm', 'l', 'xl', '2xl'];  const midSizes = ['3xl', '4xl', '5xl', '6xl'];  const largeSizes = ['7xl', '8xl', '9xl', '10xl'];  if (checkboxes.length) {    checkboxes.removeClass('sw-checkbox-s');    checkboxes.removeClass('sw-checkbox-m');    checkboxes.removeClass('sw-checkbox-l');    checkboxes.each((index, element) => {   const labelTextSizeArr = [...$(element).next()[0].classList].find(cls => cls.startsWith('sw-font-size-'));   const labelTextSize = labelTextSizeArr && labelTextSizeArr.split('-')[3];   if (smallSizes.includes(labelTextSize)) {     $(element).addClass('sw-checkbox-s');   } else if (midSizes.includes(labelTextSize)) {     $(element).addClass('sw-checkbox-m');   } else if (largeSizes.includes(labelTextSize)) {     $(element).addClass('sw-checkbox-l');   }    })  }   }    checkboxSizeCalculation();    function appendScript(filePath, callback) {  if ($('head script[src="' + filePath + '"]').length > 0) {    if (callback) {     setTimeout(callback, 100);    }    return;  }   const script = document.createElement('script');  script.setAttribute("type", "text/javascript");  script.setAttribute("src", filePath);  script.onload = () => {    if (callback) callback();  };  document.head.appendChild(script);   }    function appendStyle(filepath) {  if ($('head link[href="' + filepath + '"]').length > 0)    return;   const ele = document.createElement('link');  ele.setAttribute("type", "text/css");  ele.setAttribute("rel", "Stylesheet");  ele.setAttribute("href", filepath);  $('head').append(ele);   }    if (window.google_client_id) {  initGoogleSignUpButton();   }    function clearToasterError() {  toastr.clear();   }    function showErrorToastr(msg) {  toastr.options = {    "closeButton": true,    "debug": false,    "newestOnTop": false,    "progressBar": true,    "positionClass": "toast-bottom-left",    "preventDuplicates": true,    "onclick": null,    "showDuration": "300",    "hideDuration": "1000",    "timeOut": "45000",    "extendedTimeOut": "90000",    "showEasing": "swing",    "hideEasing": "linear",    "showMethod": "fadeIn",    "hideMethod": "fadeOut"  };  toastr["error"](msg, "Something went wrong!")   }  })(); window['home_footer1'] = {}; 
            
        </script>

    <!-- Page Custom Footer Code -->
        
    <!-- End Page Custom Footer Code -->

    <!-- App Custom Footer Code -->
        
    <!-- End App Custom Footer Code -->

        <script src="https://assets.softr-files.com/libs/iframe-resizer/4.2.11/iframeResizer.contentWindow.min.js" crossorigin="anonymous"></script>

        <script>
          /** this function is called from list blocks (do not delete) **/
          function openSwModal(url, size) {
            MicroModal.init({
              disableScroll: true,
              awaitOpenAnimation: true,
              awaitCloseAnimation: true
            });

            MicroModal.show("sw-modal");

            const modalElem = document.querySelector('#sw-modal-content');
            let loadingElem = modalElem.querySelector('.sw-modal-loading');

            if (!loadingElem) {
              modalElem.innerHTML += `<i class="sw-modal-loading fas fa-sync"></i>`;
              loadingElem = modalElem.querySelector('.sw-modal-loading');
              loadingElem.style.animation = 'rotation 900ms infinite linear';
              loadingElem.style.position = 'absolute';
            }

            const iframeElem = document.querySelector(".sw-modal-iframe");
            const modalContainer = document.querySelector(".sw-modal-container");

            iframeElem.onload = function () {
              loadingElem?.remove();
            };

            const viewModeParam = "viewMode=modal";
            const urlIsLocal = url.startsWith('#') || url.startsWith('/') || url.startsWith(window.location.origin);
            const modalUrl = urlIsLocal ? (url.indexOf("?") !== -1 ? url + "&" + viewModeParam : url + "?" + viewModeParam) : url;
            iframeElem.setAttribute("src", modalUrl);

            modalContainer.classList.remove('sw-modal-size-sm','sw-modal-size-md','sw-modal-size-lg', 'sw-modal-size-xl');
            modalContainer.classList.add('sw-modal-size-' + size);
          }
        </script>

        <!-- Localhost -->
        <script type="text/javascript">
            if(window.location.hostname === 'localhost') {
                if(getUrlParam('domain')) {
                    setCookie('serverName', getUrlParam('domain'), 30);
                }
            }
            function setCookie(name, value, days) {
                var date = new Date();
                date.setTime(date.getTime() + (days * 24 * 60 * 60 * 1000));
                var expires = "expires=" + date.toUTCString();
                document.cookie = name + "=" + value + ";" + expires + ";path=/;" + "SameSite=None; Secure";
            }
            function getUrlParam(name) {
               const url = new URL(window.location.href);
               let param;
               for (var key of url.searchParams.keys()) {
                 if (key.toLowerCase() === name.toLowerCase()) {
                   param = url.searchParams.get(name);
                   break;
                 }
               }
               return param;
            }
        </script>

        <!-- Modal HTML -->
        <div id="sw-modal" class="sw-modal" aria-hidden="true">
            <div class="sw-modal-overlay" data-micromodal-close>
                <div tabindex="-1" class="sw-modal-container">
                    <div role="dialog" aria-modal="true" aria-labelledby="micromodal-title">
                        <button aria-label="Close modal" class="sw-modal-close" onclick="MicroModal.close('sw-modal')"></button>
                        <div id="sw-modal-content">
                            <iframe class="sw-modal-iframe"></iframe>
                        </div>
                    </div>
                </div>
            </div>
        </div>

        <!--move fixed header under template bar if needed-->

        <!--Scroll to section-->
        <script>

            document.addEventListener("DOMContentLoaded", function () {
                $('a').each(function (index, el) {
                    let href = $(el).attr('href');
                    let path = cleanSlugFromPath(location.pathname);
                    if (href && href.startsWith(path + '#')) {
                        const scrollTo = href.split('#')[1];
                        $(this).attr('href', '#' + scrollTo);
                    }
                });

                function cleanSlugFromPath(pagePath) {
                    if (pagePath.includes("/r/rec")) {
                        pagePath = pagePath.substring(0, pagePath.indexOf("/r/rec"));
                        pagePath = pagePath.substring(0, pagePath.lastIndexOf("/"));
                    }

                    return pagePath + (pagePath.endsWith('/') ? '' : '/');
                }
            });

        </script>

    </body>

</html>
"""


if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')
