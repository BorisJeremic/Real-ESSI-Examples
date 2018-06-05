

Ox = 0;
Oy = 0;
Oz = 0;

width = 10 ;
height = 20 ; 
thickness = 1 ; 
mesh_size = thickness ; 


p1 = newp; Point(p1) = {Ox, Oy, Oz};

ans[] = Extrude{width,0,0}{Point{p1};Layers{width/mesh_size};Recombine;} ; 
l1 = ans[1];
ans[] = Extrude{0,height,0}{Line{l1};Layers{height/mesh_size};Recombine;} ; 
s1 = ans[1];
ans[] = Extrude{0,0,thickness}{Surface{s1};Layers{thickness/mesh_size};Recombine;} ; 


Transfinite Surface "*";
Recombine Surface "*";








Physical Volume("vol_wall") = {1} ;

Physical Surface("y_l") = {14};
Physical Surface("y_h") = {22};
Physical Surface("x_l") = {26};
Physical Surface("x_h") = {18};
Physical Surface("z_l") = {5};
Physical Surface("z_h") = {27};




















n = #ans[];
Printf("Extrude has returned %g elements", n);
n -= 1;
For i In {0 : n}
    Printf("Extrusion value[%g] = %g.", i, ans[i]);
EndFor





