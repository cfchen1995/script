% 2014-09-13

% png格式:'-dpng'
% jpeg格式:'-djpeg'
% tiff格式:'-dtiff'
% bmp格式:'-dbitmap'

close all
load('timetide-20170509.mat');
error = 1000*(up-dr');
hold on
plot(100*up)
% box off
plot(100*dr, 'r')
% 字体设置，要在相应的对象前面设置，比如xlabel，但是刻度是全局的。
set(gca,'FontName','Times New Roman','FontSize',12)
% 坐标刻度设置，可以不使用大括号
set(gca, 'XTick',0:200:1200);       % X坐标轴刻度数据点位置
set(gca,'XTickLabel',{0:2:12});     % X坐标轴刻度处显示的字符

xlabel('time/day')
ylabel('vetical displacement/cm')
legend('IERS method','Frequency method','location','best')
print(gcf,'-dtiff','displacement.tiff')

hold off
figure
plot(error,'k')
set(gca,'FontName','Times New Roman','FontSize',12)     % 字体大小设置
set(gca, 'XTick',0:200:1200);       % X坐标轴刻度数据点位置
set(gca,'XTickLabel',{0:2:12});     % X坐标轴刻度处显示的字符

xlabel('time/day')  % 坐标轴标签
ylabel('vetical displacement/mm')
print(gcf,'-dtiff','error.tiff')    % 图片保存
box off

fs = 0.05;
Y = fft(error,length(error));
amp=abs(Y);
n=0:(length(error)-1);
f=n*fs/length(error);   
plot(f(1:length(error)/2),amp(1:length(error)/2))
