% 2014-09-13

% png��ʽ:'-dpng'
% jpeg��ʽ:'-djpeg'
% tiff��ʽ:'-dtiff'
% bmp��ʽ:'-dbitmap'

close all
load('timetide-20170509.mat');
error = 1000*(up-dr');
hold on
plot(100*up)
% box off
plot(100*dr, 'r')
% �������ã�Ҫ����Ӧ�Ķ���ǰ�����ã�����xlabel�����ǿ̶���ȫ�ֵġ�
set(gca,'FontName','Times New Roman','FontSize',12)
% ����̶����ã����Բ�ʹ�ô�����
set(gca, 'XTick',0:200:1200);       % X������̶����ݵ�λ��
set(gca,'XTickLabel',{0:2:12});     % X������̶ȴ���ʾ���ַ�

xlabel('time/day')
ylabel('vetical displacement/cm')
legend('IERS method','Frequency method','location','best')
print(gcf,'-dtiff','displacement.tiff')

hold off
figure
plot(error,'k')
set(gca,'FontName','Times New Roman','FontSize',12)     % �����С����
set(gca, 'XTick',0:200:1200);       % X������̶����ݵ�λ��
set(gca,'XTickLabel',{0:2:12});     % X������̶ȴ���ʾ���ַ�

xlabel('time/day')  % �������ǩ
ylabel('vetical displacement/mm')
print(gcf,'-dtiff','error.tiff')    % ͼƬ����
box off

fs = 0.05;
Y = fft(error,length(error));
amp=abs(Y);
n=0:(length(error)-1);
f=n*fs/length(error);   
plot(f(1:length(error)/2),amp(1:length(error)/2))
