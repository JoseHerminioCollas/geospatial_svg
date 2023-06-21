logo = """<g transform="translate(135,285) scale(0.4)" fill="black" stroke="none">
<path
         d="m 6.909225,12.189723 h 3.199798 l 3.274213,9.11157 3.265944,-9.11157 h 3.199798 l -4.572322,12.344441 h -3.795109 z"
         style="font-size:16.9333px;stroke-width:0.265"
         id="path428" />
      <path
         d="M 27.827804,22.285211 H 22.85034 l -0.78548,2.248953 h -3.199799 l 4.572322,-12.344441 h 3.79511 l 4.572321,12.344441 h -3.199798 z m -4.183716,-2.290295 h 3.381699 l -1.686715,-4.911319 z"
         style="font-size:16.9333px;stroke-width:0.265"
         id="path430" />
      <path
         d="m 37.964634,17.66328 q 1.000454,0 1.430401,-0.37207 0.438215,-0.37207 0.438215,-1.223696 0,-0.843357 -0.438215,-1.207159 -0.429947,-0.363801 -1.430401,-0.363801 h -1.33945 v 3.166726 z m -1.33945,2.199344 v 4.67154 H 33.441922 V 12.189723 h 4.861709 q 2.439123,0 3.571868,0.818553 1.141013,0.818553 1.141013,2.58795 0,1.223696 -0.595311,2.009176 -0.587043,0.78548 -1.777666,1.15755 0.653189,0.148828 1.165818,0.677993 0.520898,0.520898 1.050063,1.587497 l 1.728057,3.505722 h -3.389967 l -1.504815,-3.067507 q -0.454752,-0.926039 -0.92604,-1.265036 -0.46302,-0.338997 -1.240232,-0.338997 z"
         style="font-size:16.9333px;stroke-width:0.265"
         id="path432" />
      <path
         d="m 46.480893,12.189723 h 3.183262 v 12.344441 h -3.183262 z"
         style="font-size:16.9333px;stroke-width:0.265"
         id="path434" />
      <path
         d="m 62.570834,23.856171 q -0.876431,0.454752 -1.827275,0.686262 -0.950845,0.23151 -1.984371,0.23151 -3.084044,0 -4.886514,-1.719789 -1.802471,-1.728056 -1.802471,-4.679808 0,-2.96002 1.802471,-4.679809 1.80247,-1.728056 4.886514,-1.728056 1.033526,0 1.984371,0.23151 0.950844,0.23151 1.827275,0.686261 v 2.554878 q -0.884699,-0.603579 -1.744593,-0.884699 -0.859894,-0.281119 -1.810739,-0.281119 -1.703252,0 -2.678901,1.091404 -0.975649,1.091404 -0.975649,3.00963 0,1.909957 0.975649,3.001361 0.975649,1.091404 2.678901,1.091404 0.950845,0 1.810739,-0.281119 0.859894,-0.281119 1.744593,-0.884699 z"
         style="font-size:16.9333px;stroke-width:0.265"
         id="path436" />
      <path
         d="m 65.208394,12.189723 h 3.183262 v 12.344441 h -3.183262 z"
         style="font-size:16.9333px;stroke-width:0.265"
         id="path438" />
      <path
         d="m 70.037033,12.189723 h 11.377061 v 2.40605 h -4.092766 v 9.938391 h -3.183262 v -9.938391 h -4.101033 z"
         style="font-size:16.9333px;stroke-width:0.265"
         id="path440" />
      <path
         d="m 83.059464,12.189723 h 8.590673 v 2.40605 h -5.407411 v 2.298563 h 5.084951 v 2.40605 h -5.084951 v 2.827728 h 5.589312 v 2.40605 h -8.772574 z"
         style="font-size:16.9333px;stroke-width:0.265"
         id="path442" />
         </g>
"""
def writeSVG(fileName, data):
    f = open(fileName, 'w')
    tagString = '<circle r="{0}" cx="{2}mm" cy="{1}mm" fill="none" stroke="black" stroke-width="0.1mm" />'
    f.write('<svg width="80mm" height="80mm" fill="none" stroke="black">')
    f.write('<circle r="40mm" cx="40mm" cy="40mm" stroke-width="0.1mm" />')
    for e in data:
        offset = 40
        x = e['x'] + offset
        y = e['y'] + offset
        circleSVG = tagString.format(e['circleRadius'], y, x)
        f.write(circleSVG)
    f.write(logo)
    f.write('</svg>')
