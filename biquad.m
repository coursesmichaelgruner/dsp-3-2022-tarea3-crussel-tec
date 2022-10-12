clear;

fs=8000;

f0=440;
w0=f0*pi/180;

N=400;

y=zeros(N,1);
x=zeros(N,1);
x(100)=1;

r=1.000001;

a1=-2*r*cos(w0*fs);
a2=r*r;
b0=0;
b1=r*sin(w0*fs);
b2=0;

for n=3:1:N
  y(n)=b0*x(n)+b1*x(n-1)+b2*x(n-2)-a1*y(n-1)-a2*y(n-2);
endfor

clf;
plot(y);
hold on;

for n=100:1:N
  yy(n)=(r^(n-100))*sin(w0*(n-100)*fs);
endfor

plot(yy);
