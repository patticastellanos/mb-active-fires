#fires {
  marker-comp-op:lighten;
  marker-file:url("flame.png");
  marker-allow-overlap:true;
  marker-transform:"scale(0.07)";
  [fires >=0] {marker-opacity:0.3;}
  [fires >=10] {marker-opacity:0.4;}
  [fires >=20] {marker-opacity:0.5;}
  [fires >=40] {marker-opacity:0.6;}
  [fires >=60] {marker-opacity:0.7;}
  [fires >=80] {marker-opacity:0.8;}
  [fires = 100] {marker-opacity:0.9;}
  
  [zoom>=0] { marker-transform:"scale([fires^0.5]*0.015)"; }
  [zoom>=1] { marker-transform:"scale(0.1*[fires^0.5]*0.02)"; }
  [zoom>=2] { marker-transform:"scale(0.1*[fires^0.5]*0.01)"; }
  [zoom>=3] { marker-transform:"scale(0.1*[fires^0.5]*0.02)"; }
  [zoom>=4] { marker-transform:"scale([fires]*0.04)"; }
  [zoom>=5] { marker-transform:"scale(0.1*[fires^0.5]*0.08)"; }
  [zoom>=6] { marker-transform:"scale(0.1*[fires^0.5]*5)"; }

}