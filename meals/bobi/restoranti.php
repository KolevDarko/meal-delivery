<!DOCTYPE html>
<html lang="en">

<head>

    <meta charset="utf-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, shrink-to-fit=no, initial-scale=1">
    <meta name="description" content="">
    <meta name="author" content="">

    <title>ОнЛајн Храна</title>

    <!-- Bootstrap Core CSS -->
    <link href="css/bootstrap.min.css" rel="stylesheet">

    <!-- Custom CSS -->
    <link href="css/simple-sidebar.css" rel="stylesheet">

    <link href="css/navbar-fixed-side.css" rel="stylesheet" />
</head>

<body>



<div class="container-fluid">
    <div class="row">
        <?php
        require('includes/html/main-header.php');
        ?>
        <div class="col-lg-10">
            <div class="row">
                <div class="container-fluid">

                    <center><h1>Ресторанти</h1></center>
                    <img src="images/slider1.jpg" class="img-responsive main-image" height="100">

                    <p>This template has a responsive menu toggling system. The menu will appear collapsed on smaller screens, and will appear non-collapsed on larger screens. When toggled using the button below, the menu will appear/disappear. On small screens, the page content will be pushed off canvas.</p>

                </div>
            </div>

            <div class="row-sredina">

                <h3>Наша препорака</h3>

                <div class="container">
                    <div class="col-md-11">


                        <div class="well-none">
                            <div id="myCarousel" class="carousel slide">

                                <!-- Carousel items -->
                                <div class="carousel-inner">
                                    <div class="item active">
                                        <div class="row">

                                            <div class="col-sm-3 col-xs-3 col-lg-3 col-md-3">
                                                <div class="container-a">
                                                    <a href= "aledar.php" ><img src="images/aledar.jpg" alt="Image" class="img-responsive" width="220" height="220"></a>
                                                    <div class="overlay-a">
                                                        <div class="text-a">
                                                            <p> Достава: онлајнјадење </p>
                                                            <p> Цена за достава: 50 денари </p>
                                                            <p> Мин. нарачка: 250ден. + достава </p>
                                                            <p> Цена за достава: 50 денари </p>
                                                            <p> Плаќање: во готово/со картица </p></div>
                                                    </div>
                                                </div>
                                                <p>
                                                    <img style="float: left; margin: 5px;" ... />
                                                   <a href="aledar.php"> АЛЕ-ДАР </a>
                                                </p>
                                            </div>

                                            <div class="col-sm-3 col-xs-3 col-lg-3 col-md-3">
                                                <div class="container-a">
                                                    <a href="pace.php"><img src="images/pace.jpg" alt="Image" class="img-responsive" width="220" height="220"></a>
                                                    <div class="overlay-a">
                                                        <div class="text-a">
                                                            <p> Достава: онлајнјадење </p>
                                                            <p> Цена за достава: 50 денари </p>
                                                            <p> Мин. нарачка: 250ден. + достава </p>
                                                            <p> Цена за достава: 50 денари </p>
                                                            <p> Плаќање: во готово/со картица </p>
                                                        </div>
                                                    </div>
                                                </div>
                                                <p>
                                                    <img style="float: left; margin: 5px;"  />
                                                    <a href="pace.php"> ПАЦЕ </a>
                                                </p>
                                            </div>

                                            <div class="col-sm-3 col-xs-3 col-lg-3 col-md-3">
                                                <div class="container-a">
                                                    <a href="ogniste.php"><img src="images/ogniste.jpg" alt="Image" class="img-responsive" width="220" height="220"></a>
                                                    <div class="overlay-a">
                                                        <div class="text-a">
                                                            <p> Достава: онлајнјадење </p>
                                                            <p> Цена за достава: 50 денари </p>
                                                            <p> Мин. нарачка: 250ден. + достава </p>
                                                            <p> Цена за достава: 50 денари </p>
                                                            <p> Плаќање: во готово/со картица </p>
                                                        </div>
                                                    </div>
                                                </div>
                                                <p>
                                                    <img style="float: left; margin: 5px;"  />
                                                    <a href="ogniste.php"> ОГНИШТЕ </a>
                                                </p>
                                            </div>

                                            <div class="col-sm-3 col-xs-3 col-lg-3 col-md-3">
                                                <div class="container-a">
                                                    <a href="#x"><img src="http://placehold.it/500x500" alt="Image" class="img-responsive" width="220" height="220"></a>
                                                    <div class="overlay-a">
                                                        <div class="text-a">
                                                            <p> Достава: онлајнјадење </p>
                                                            <p> Цена за достава: 50 денари </p>
                                                            <p> Мин. нарачка: 250ден. + достава </p>
                                                            <p> Цена за достава: 50 денари </p>
                                                            <p> Плаќање: во готово/со картица </p>
                                                        </div>
                                                    </div>
                                                </div>
                                                <p>
                                                    <img style="float: left; margin: 5px;"  />
                                                    Text goes here
                                                </p>
                                            </div>

                                        </div>
                                        <!--/row-->
                                    </div>

                                    <!--/row-->
                                </div>
                                <!--/item-->

                                <!--/item-->
                            </div>
                            <!--/carousel-inner-->
                            <!-- ostaveno za nekoj pat ako ima vrtenje
                            <a class="left carousel-control" href="#myCarousel" data-slide="prev"><i class="fa fa-chevron-left fa-4"></i></a>

                            <a class="right carousel-control" href="#myCarousel" data-slide="next"><i class="fa fa-chevron-right fa-4"></i></a>
                            -->
                        </div>
                        <!--/myCarousel-->
                    </div>
                    <!--/well-->
                </div>
            </div>

            <div class="container-fluid">
                <div class="row-sredina">
                    <div class="col-lg-20">
                        <center><h2>Сите</h2></center>

                        <div class="container">
                            <div class="col-md-11">


                                <div class="well-none">
                                    <div id="myCarousel" class="carousel slide">

                                        <!-- Carousel items -->
                                        <div class="carousel-inner">
                                            <div class="item active">
                                                <div class="row">

                                                    <div class="col-sm-3 col-xs-3 col-lg-3 col-md-3">
                                                        <div class="container-a">
                                                            <a href="#x"><img src="http://placehold.it/500x500" alt="Image" class="img-responsive" width="220" height="220"></a>
                                                            <div class="overlay-a">
                                                                <div class="text-a">Hello World</div>
                                                            </div>
                                                        </div>
                                                        <p>
                                                            <img style="float: left; margin: 5px;"  />
                                                            Text goes here...
                                                        </p>
                                                    </div>

                                                    <div class="col-sm-3 col-xs-3 col-lg-3 col-md-3">
                                                        <div class="container-a">
                                                            <a href="#x"><img src="http://placehold.it/500x500" alt="Image" class="img-responsive" width="220" height="220"></a>
                                                            <div class="overlay-a">
                                                                <div class="text-a">Hello World</div>
                                                            </div>
                                                        </div>
                                                        <p>
                                                            <img style="float: left; margin: 5px;"  />
                                                            Text goes here...
                                                        </p>
                                                    </div>

                                                    <div class="col-sm-3 col-xs-3 col-lg-3 col-md-3">
                                                        <div class="container-a">
                                                            <a href="#x"><img src="http://placehold.it/500x500" alt="Image" class="img-responsive" width="220" height="220"></a>
                                                            <div class="overlay-a">
                                                                <div class="text-a">Hello World</div>
                                                            </div>
                                                        </div>
                                                        <p>
                                                            <img style="float: left; margin: 5px;"  />
                                                            Text goes here...
                                                        </p>
                                                    </div>

                                                    <div class="col-sm-3 col-xs-3 col-lg-3 col-md-3">
                                                        <div class="container-a">
                                                            <a href="#x"><img src="http://placehold.it/500x500" alt="Image" class="img-responsive" width="220" height="220"></a>
                                                            <div class="overlay-a">
                                                                <div class="text-a">Hello World</div>
                                                            </div>
                                                        </div>
                                                        <p>
                                                            <img style="float: left; margin: 5px;"  />
                                                            Text goes here...
                                                        </p>
                                                    </div>

                                                    <div class="col-sm-3 col-xs-3 col-lg-3 col-md-3">
                                                        <div class="container-a">
                                                            <a href="#x"><img src="http://placehold.it/500x500" alt="Image" class="img-responsive" width="220" height="220"></a>
                                                            <div class="overlay-a">
                                                                <div class="text-a">Hello World</div>
                                                            </div>
                                                        </div>
                                                        <p>
                                                            <img style="float: left; margin: 5px;"  />
                                                            Text goes here...
                                                        </p>
                                                    </div>

                                                    <div class="col-sm-3 col-xs-3 col-lg-3 col-md-3">
                                                        <div class="container-a">
                                                            <a href="#x"><img src="http://placehold.it/500x500" alt="Image" class="img-responsive" width="220" height="220"></a>
                                                            <div class="overlay-a">
                                                                <div class="text-a">Hello World</div>
                                                            </div>
                                                        </div>
                                                        <p>
                                                            <img style="float: left; margin: 5px;"  />
                                                            Text goes here...
                                                        </p>
                                                    </div>

                                                    <div class="col-sm-3 col-xs-3 col-lg-3 col-md-3">
                                                        <div class="container-a">
                                                            <a href="#x"><img src="http://placehold.it/500x500" alt="Image" class="img-responsive" width="220" height="220"></a>
                                                            <div class="overlay-a">
                                                                <div class="text-a">Hello World</div>
                                                            </div>
                                                        </div>
                                                        <p>
                                                            <img style="float: left; margin: 5px;"  />
                                                            Text goes here...
                                                        </p>
                                                    </div>

                                                    <div class="col-sm-3 col-xs-3 col-lg-3 col-md-3">
                                                        <div class="container-a">
                                                            <a href="#x"><img src="http://placehold.it/500x500" alt="Image" class="img-responsive" width="220" height="220"></a>
                                                            <div class="overlay-a">
                                                                <div class="text-a">Hello World</div>
                                                            </div>
                                                        </div>
                                                        <p>
                                                            <img style="float: left; margin: 5px;"  />
                                                            Text goes here...
                                                        </p>
                                                    </div>

                                                    <div class="col-sm-3 col-xs-3 col-lg-3 col-md-3">
                                                        <div class="container-a">
                                                            <a href="#x"><img src="http://placehold.it/500x500" alt="Image" class="img-responsive" width="220" height="220"></a>
                                                            <div class="overlay-a">
                                                                <div class="text-a">Hello World</div>
                                                            </div>
                                                        </div>
                                                        <p>
                                                            <img style="float: left; margin: 5px;"  />
                                                            Text goes here...
                                                        </p>
                                                    </div>

                                                    <div class="col-sm-3 col-xs-3 col-lg-3 col-md-3">
                                                        <div class="container-a">
                                                            <a href="#x"><img src="http://placehold.it/500x500" alt="Image" class="img-responsive" width="220" height="220"></a>
                                                            <div class="overlay-a">
                                                                <div class="text-a">Hello World</div>
                                                            </div>
                                                        </div>
                                                        <p>
                                                            <img style="float: left; margin: 5px;"  />
                                                            Text goes here...
                                                        </p>
                                                    </div>

                                                </div>
                                            </div>
                                        </div>
                                    </div>
                                </div>
                                <!--/myCarousel-->
                            </div>
                            <!--/well-->
                        </div>
                    </div>
                </div>

            </div>

        </div>
    </div>

</div>
</div>


<!--kraj na moe meni-->





<!-- Page Content -->



<!-- /#wrapper -->

<!-- jQuery -->
<script src="js/jquery.js"></script>

<!-- Bootstrap Core JavaScript -->
<script src="js/bootstrap.min.js"></script>
<!-- My Styles -->
<link rel="stylesheet" href="css/mojcss.css">
<!-- Menu Toggle Script -->
<script>
    $("#menu-toggle").click(function(e) {
        e.preventDefault();
        $("#wrapper").toggleClass("toggled");
    });
</script>

<script>
    $(function () {
        $('.showFirst').click(function () {
            $(this).children('ul').slideToggle();
            $('.showFirst > li').not(this).find('ul').slideUp();
        });
        $('.showSecond').click(function () {
            $(this).children('ul').slideToggle("slow");
        });

    });
</script>

<script>
    $('#myCarousel').carousel({
        interval: 0
    })

    $('#myCarousel').on('slid.bs.carousel', function() {
        alert("slid");
    });
</script>


</body>

</html>
