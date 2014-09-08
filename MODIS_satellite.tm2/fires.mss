#fires {
  marker-comp-op:lighten;
  marker-file:url("flame.png");
  marker-allow-overlap:true;
  //marker-transform:"scale(2.0)";
  [fires >=0] {marker-opacity:1;}
  [fires >=10] {marker-opacity:1;}
  [fires >=20] {marker-opacity:1;}
  [fires >=40] {marker-opacity:0.5;}
  [fires >=60] {marker-opacity:0.5;}
  [fires >=80] {marker-opacity:0.5;}
  [fires = 100] {marker-opacity:0.5;}
  
  [zoom>=0] { marker-transform:"scale([fires]*0.0025)"; }
  [zoom>=1] { marker-transform:"scale([fires]*0.005)"; }
  [zoom>=2] { marker-transform:"scale([fires]*0.01)"; }
  [zoom>=3] { marker-transform:"scale([fires]*0.02)"; }
  [zoom>=4] { marker-transform:"scale([fires]*0.04)"; }
  [zoom>=5] { marker-transform:"scale([fires]*0.08)"; }
  [zoom>=6] { marker-transform:"scale([fires]*0.16)"; }

}