// Languages: name (local), name_en, name_fr, name_es, name_de
@name: '[name_en]';

@sans: 'Meta Offc Pro Cond Normal', 'Arial Unicode MS Regular';
@sans_it: 'Meta Offc Pro Light Italic', 'Arial Unicode MS Regular';
@serif_md: 'Meta Serif SC Offc Pro Medium', 'Arial Unicode MS Regular';

#country_label {
  text-name: @name;
  text-face-name: @serif_md;
  text-fill: #ed8;
  text-halo-fill: fadeout(darken(@water,10),95);
  text-halo-radius: 3;
  text-halo-rasterizer: fast;
  [zoom>=3] {
    text-size: 10;
    [scalerank<=6] { text-size: 12; }
    [scalerank<=4] { text-size: 14; }
    [scalerank<=2] { text-size: 16; }
  }
  [zoom>=5] {
    text-size: 11;
    [scalerank<=6] { text-size: 14; }
    [scalerank<=4] { text-size: 17; }
    [scalerank<=2] { text-size: 20; }
  }
  [zoom>=6] {
    text-size: 14;
    [scalerank<=6] { text-size: 18; }
    [scalerank<=4] { text-size: 22; }
    [scalerank<=2] { text-size: 26; }
  }
}

// City labels with dots for low zoom levels.
// The separate attachment keeps the size of the XML down.
#place_label::citydots[zoom>=4][localrank<=2] {
  // explicitly defining all the `ldir` values wer'e going
  // to use shaves a bit off the final project.xml size
  [ldir='N'],[ldir='S'],[ldir='E'],[ldir='W'],
  [ldir='NE'],[ldir='SE'],[ldir='SW'],[ldir='NW'] {
    shield-file: url("img/dot-3.png");
    shield-unlock-image: true;
    shield-name: @name;
    shield-face-name: @sans;
    shield-placement: point;
    shield-fill: white;
    shield-halo-fill: fadeout(@water,90);
    shield-halo-radius: 2;
    shield-halo-rasterizer: fast;
    shield-min-distance: 3;
    //shield-wrap-width: 40;
    shield-line-spacing: -4;
    shield-size: 13;
    [zoom>=5] {
      [scalerank>=0][scalerank<=2] { shield-size: 16; }
      [scalerank>=3][scalerank<=5] { shield-size: 14; }
    }
    [zoom>=6] {
      [scalerank>=0][scalerank<=2] { shield-size: 18; }
      [scalerank>=3][scalerank<=5] { shield-size: 16; }
    }
    [zoom>=7] {
      shield-size: 14;
      [scalerank>=0][scalerank<=2] { shield-size: 20; }
      [scalerank>=3][scalerank<=5] { shield-size: 18; }
      [scalerank>=6] { shield-size: 16; }
    }
    [zoom>=8] {
      shield-size: 16;
      [scalerank>=0][scalerank<=2] { shield-size: 28; }
      [scalerank>=3][scalerank<=5] { shield-size: 22; }
      [scalerank>=6] { shield-size: 18; }
    }
    [ldir='E'] { shield-text-dx: 5; }
    [ldir='W'] { shield-text-dx: -5; }
    [ldir='N'] { shield-text-dy: -5; }
    [ldir='S'] { shield-text-dy: 8; }
    [ldir='NE'] { shield-text-dx: 4; shield-text-dy: -3; }
    [ldir='SE'] { shield-text-dx: 4; shield-text-dy: 5; }
    [ldir='SW'] { shield-text-dx: -4; shield-text-dy: 5; }
    [ldir='NW'] { shield-text-dx: -4; shield-text-dy: -3; }
  }
}

#water_label {
  [zoom<=15][area>200000],
  [zoom=16][area>50000],
  [zoom=17][area>10000],
  [zoom>=18][area>0]{
    text-name: @name;
    text-size: 14;
    text-line-spacing: -2;
    text-face-name: @sans_it;
    text-fill: #abc;
    text-halo-fill: fadeout(@water,85);
    text-halo-radius: 2;
    text-halo-rasterizer: fast;
  }
}