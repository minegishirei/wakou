
<template>
    <!DOCTYPE html>
    <html lang="en">

    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>All Products | RedStore</title>
        <link rel="stylesheet" href="style.css">
        <link href="https://fonts.googleapis.com/css2?family=Poppins:wght@300;400;500;600;700&display=swap"
            rel="stylesheet">
        <link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/font-awesome/4.7.0/css/font-awesome.min.css">
    </head>

    <body>
        <div class="container">
            <div class="navbar">
                <div class="logo">
                    <a href="index.html"><img src="images/logo.png" alt="logo" width="125px"><b>和光イベントカレンダー</b></a>

                </div>
                <nav>
                    <ul id="MenuItems">
                        <li><a href="index.html">Home</a></li>
                        <li><a href="products.html">Products</a></li>
                        <li><a href="">About</a></li>
                        <li><a href="">Contact</a></li>
                        <li><a href="account.html">Account</a></li>
                    </ul>
                </nav>
                <a href="cart.html"><img src="images/cart.png" width="30px" height="30px"></a>
                <img src="images/menu.png" class="menu-icon" onclick="menutoggle()">
            </div>
        </div>

        <!-- Single Products -->
        <div class="small-container single-product">
            <div class="row">
                <div class="col-3">
                    <div v-for="image in images" :key="image">
                        <img :src="image" width="100%" id="ProductImg" >
                    </div>
                </div>
                <div class="col-2">
                    <p>Home / T-Shirt</p>
                    <h1>{{ title }}</h1>
                    <h4>{{ date }} {{ open_at }}</h4>

                    <h3>イベント詳細 <i class="fa fa-indent"></i></h3>
                    <p>{{ description }}</p>
<br>
                    <h3>開催 <i class="fa fa-indent"></i></h3>
                    <p>{{ ask }}</p>

<br>
                    <h3>料金 <i class="fa fa-indent"></i></h3>
                    <p>{{ fee }}</p>

<br>
                    <h3>場所 <i class="fa fa-indent"></i></h3>
                    <p>{{ location }}</p>
                    <!--
                    <select>
                        <option>Select Size</option>
                        <option>XXL</option>
                        <option>XL</option>
                        <option>L</option>
                        <option>M</option>
                        <option>S</option>
                    </select>
                    <input type="number" value="1">
                    <a href="" class="btn">Add To Cart</a>
                    -->

                    <!--

                            "20230517153633": {
        "date": " 令和5年8月22日（火曜日）",
        "open_at": " 14：00 ",
        "location": " 小ホール",
        "fee": " 全席自由 2,800円（税込） 【サンアゼリア友の会会員 2,500円（税込）】 ※未就学のお子様のご入場はご遠慮ください。",
        "detail_link": "https://www.sunazalea.or.jp/event/detail.cgi?key=20230517153633",
        "ask": " サンアゼリア 048-468-7771 ",
        "title": "和光市/和光市民文化センターサンアゼリア開館30周年記念 サンアゼリア寄席 柳亭明楽真打昇進披露公演",
        "images": [
            "https://www.sunazalea.or.jp/event/log/img/20230517153633_1.jpg"
        ],
        "id": "20230517153633"
    },
                    -->

                    <br>
                </div>
            </div>
        </div>
        <!-- title -->
        <div class="small-container">
            <div class="row row-2">
                <h2>Related Products</h2>
                <p>View More</p>
            </div>
        </div>

        <div class="categories">
            <div class="small-container">
                <div class="row">
                    <div class="col-4" v-for="(item, key) in store_top4" :key="key">
                        <a v-bind:href="`product_details.html?id=${item.id}`">
                            <img v-bind:src="`${item.images[1]? item.images[1] : item.images[0]}`">
                        </a>
                        <h4>{{ item.title }}</h4>

                        <p>{{ item.date }}</p>
                    </div>
                </div>
            </div>
        </div>
        <!-- Footer -->
        <div class="footer">
            <div class="container">
                <div class="row">
                    <div class="footer-col-1">
                        <h3>Download Our App</h3>
                        <p>Download App for Android and ios mobile phone.</p>
                        <div class="app-logo">
                            <img src="images/play-store.png">
                            <img src="images/app-store.png">
                        </div>
                    </div>
                    <div class="footer-col-2">
                        <img src="images/logo-white.png">
                        <p>Our Purpose Is To Sustainably Make the Pleasure and Benefits of Sports Accessible to the Many.
                        </p>
                    </div>
                    <div class="footer-col-3">
                        <h3>Useful Links</h3>
                        <ul>
                            <li>Coupons</li>
                            <li>Blog Post</li>
                            <li>Return Policy</li>
                            <li>Join Affiliate</li>
                        </ul>
                    </div>
                    <div class="footer-col-4">
                        <h3>Follow Us</h3>
                        <ul>
                            <li>Facebook</li>
                            <li>Twitter</li>
                            <li>Instagram</li>
                            <li>Youtube</li>
                        </ul>
                    </div>
                </div>
                <hr>
                <p class="copyright">Copyright 2020 - Samwit Adhikary</p>
            </div>
        </div>

        <!-- javascript -->
        <component :is="'script'">
            var MenuItems = document.getElementById("MenuItems");
            MenuItems.style.maxHeight = "0px";
            function menutoggle() {
            if (MenuItems.style.maxHeight == "0px") {
            MenuItems.style.maxHeight = "200px"
            }
            else {
            MenuItems.style.maxHeight = "0px"
            }
            }
        </component>
        <!-- product gallery -->

        <component :is="'script'">
            var ProductImg = document.getElementById("ProductImg");
            var SmallImg = document.getElementsByClassName("small-img");

            SmallImg[0].onclick = function () {
            ProductImg.src = SmallImg[0].src;
            }
            SmallImg[1].onclick = function () {
            ProductImg.src = SmallImg[1].src;
            }
            SmallImg[2].onclick = function () {
            ProductImg.src = SmallImg[2].src;
            }
            SmallImg[3].onclick = function () {
            ProductImg.src = SmallImg[3].src;
            }
        </component>
    </body>

    </html>
</template>

<script>
import store from "../store/store";
export default {
    name: 'WakouProductDetails',
    data() {
        document.title = store[this.$route.query.id].title
        return Object.assign(
            store[this.$route.query.id],
            store[this.$route.query.id],
            {
                store: store,
                store_top4: Object.fromEntries(Object.entries(store).slice(0, 4)),
        })
    }
}
</script>
