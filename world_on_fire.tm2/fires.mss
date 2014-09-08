/*#modis_fire_201001_201012 {
  point-comp-op:lighten;
  point-opacity:0.35;
  point-file:url(flame_on_flame.svg);
  point-allow-overlap:true;
  [zoom>=0] { point-transform:"scale([fires]*0.000005)"; }
  [zoom>=1] { point-transform:"scale([fires]*0.00001)"; }
  [zoom>=2] { point-transform:"scale([fires]*0.00002)"; }
  [zoom>=3] { point-transform:"scale([fires]*0.00004)"; }
  [zoom>=4] { point-transform:"scale([fires]*0.00008)"; }
  [zoom>=5] { point-transform:"scale([fires]*0.00016)"; }
  [zoom>=6] { point-transform:"scale([fires]*0.00032)"; }
}*/

/*#modis_fire_201001_201012 {
  image-filters:colorize-alpha(blue, cyan, green, yellow , orange, red);
  comp-op:multiply;
  marker-allow-overlap:true;
  marker-file:url(flame_on_flame.svg);
  marker-width:0.6;
}*/

#fires {
  //point-comp-op:lighten;
  point-opacity:0.35;
  point-file:url(flame.png);
  point-allow-overlap:true;
  point-transform:"scale(0.02)";
  [fires >=0] {point-opacity:0.3;}
  [fires >=10] {point-opacity:0.4;}
  [fires >=20] {point-opacity:0.5;}
  [fires >=40] {point-opacity:0.6;}
  [fires >=60] {point-opacity:0.7;}
  [fires >=80] {point-opacity:0.8;}
  [fires = 100] {point-opacity:0.9;}
  
  [zoom>=0] { point-transform:"scale(0.1*[fires]*0.0025)"; }
  [zoom>=1] { point-transform:"scale(0.1*[fires]*0.02)"; }
  [zoom>=2] { point-transform:"scale(0.1*[fires]*0.01)"; }
  [zoom>=3] { point-transform:"scale(0.1*[fires]*0.02)"; }
  [zoom>=4] { point-transform:"scale(0.1*[fires]*0.04)"; }
  [zoom>=5] { point-transform:"scale(0.1*[fires]*0.08)"; }
  [zoom>=6] { point-transform:"scale(0.1*[fires]*0.16)"; }

}
/*#fires{
  raster-opacity:0.35;
  raster-colorizer-default-mode:linear;
}*/
