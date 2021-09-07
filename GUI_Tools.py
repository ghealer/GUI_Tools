# -*- coding: utf-8 -*-
import wx
import GUI_Tools_wxpython_gui
import subprocess
from setting import java8_path
from setting import java9_path

class MianWindow(GUI_Tools_wxpython_gui.jar_management_gui):

    #webshell管理工具
    def godzilla_click(self, event):
        subprocess.Popen("cd gui_webshell/Godzilla && " + java8_path + ' -jar ' + 'Godzilla.jar', shell=True)

    def behinder_click(self, event):
        subprocess.Popen("cd gui_webshell/Behinder && " + java8_path + ' -jar ' + 'Behinder.jar', shell=True)

    #渗透工具
    def burp_suite_click(self, event):
        subprocess.Popen("cd gui_other/burpsuite_pro_v2021.5.1 && " + java9_path + ' --illegal-access=permit -Dfile.encoding=utf-8 -javaagent:BurpSuiteLoader_v2021.8.1.jar -noverify -jar burpsuite_pro_v2021.8.jar', shell=True)

    def cs_click(self, event):
        subprocess.Popen("cd gui_other/cobaltstrike4.3/cobaltstrike4.3 && " + java8_path + ' -XX:ParallelGCThreads=4 -XX:+AggressiveHeap -XX:+UseParallelGC -jar cobaltstrike.jar', shell=True)

    #信息收集
    def dirscan_click(self, event):
        subprocess.Popen("cd gui_shouji/dirscan_3.0 && " + java9_path + ' -jar ' + 'scandir-3.0.jar', shell=True)
    def webfinder_click(self, event):
        subprocess.Popen("cd gui_shouji && " + java8_path + ' -jar ' + 'webfinder-3.2.jar', shell=True)
    def fofa_click(self, event):
        subprocess.Popen("cd gui_shouji/fofaviewer_1.0.7_ && " + java8_path + ' -jar ' + 'fofaviewer.jar', shell=True)
    def yj_click(self, event):
        subprocess.Popen('cd gui_shouji/yjdirscanv1.1 && 御剑目录扫描专业版v1.1.exe', shell=True)


    #漏洞扫描
    def tdoa_click(self, event):
        subprocess.Popen("cd gui_scan && " + java8_path + ' -jar ' + 'TODA.jar', shell=True)

    def gr33k_click(self, event):
        subprocess.Popen('python3 gui_scan/Gr33k/Gr33k.py', shell=True)

    def cas_click(self, event):
        subprocess.Popen("cd gui_scan && " + java8_path + ' -jar ' + 'CAS_cc2_Exploit-1.0-SNAPSHOTv1.1-all.jar', shell=True)

    def sj_click(self, event):
        subprocess.Popen("cd gui_scan && " + java8_path + ' -jar ' + 'SJ-V1.9.jar', shell=True)

    def thinkphp_click(self, event):
        subprocess.Popen("cd gui_scan/thinkphp && " + java8_path + ' -jar ' + 'ThinkPHP.V2.0.by.jar', shell=True)

    def thinkphp_log_click(self, event):
        subprocess.Popen('cd gui_scan/thinkphp && ThinkPHP.v1.2_Beta.exe', shell=True)

    def thinkphp1_click(self, event):
        subprocess.Popen("cd gui_scan/thinkphp && " + java8_path + ' -jar ' + 'ThinkphpGUI-1.2-SNAPSHOT.jar', shell=True)

    def thinkphp2_click(self, event):
        subprocess.Popen("cd gui_scan/thinkphp && " + java8_path + ' -jar ' + 'thinkphp命令执行检测工具.jar', shell=True)

    def weblogic_click(self, event):
        subprocess.Popen("cd gui_scan/weblogic/weblogic-framework-0.2.3 && " + java8_path + ' -jar ' + 'weblogic-framework-0.2.3-all-jar-with-dependencies.jar', shell=True)

    def weblogic1_click(self, event):
        subprocess.Popen("cd gui_scan/weblogic && " + java8_path + ' -jar ' + 'weblogic_exploit-1.0-SNAPSHOT-all.jar', shell=True)

    def edr_click(self, event):
        subprocess.Popen("cd gui_scan && " + java8_path + ' -jar ' + '深X服edr任意用户登陆检测工具.jar', shell=True)

    def shiro_attack_click(self, event):
        subprocess.Popen("cd gui_scan/shiro/shiro_attack_2.2 && " + java8_path + ' -jar ' + 'shiro_attack-2.2.jar', shell=True)

    def shiroexp_click(self, event):
        subprocess.Popen("cd gui_scan/shiro && " + java8_path + ' -jar ' + 'ShiroExp.jar', shell=True)

    def shiroexploit_click(self, event):
        subprocess.Popen("cd gui_scan/shiro && " + java8_path + ' -jar ' + 'ShiroExploit-v2.3.jar', shell=True)

    def shiroexploit1_cilck(self, event):
        subprocess.Popen("cd gui_scan/shiro && " + java8_path + ' -jar ' + 'ShiroExploit.jar', shell=True)

    def shiroscan_click(self, event):
        subprocess.Popen("cd gui_scan/shiro && " + java8_path + ' -jar ' + 'ShiroScan-1.1.jar', shell=True)

    def shiro1_click(self, event):
        subprocess.Popen("cd gui_scan/shiro/ShiroExploit.V2.51 && " + java8_path + ' -jar ' + 'ShiroExploit.jar', shell=True)

    def oracleshell_click(self, event):
        subprocess.Popen("cd gui_scan && " + java8_path + ' -jar ' + 'oracleShell.jar', shell=True)

    def framescan_click(self, event):
        subprocess.Popen("cd gui_scan/FrameScan-GUI && FrameScan-GUI.exe", shell=True)

    def tomcat_password_click(self, event):
        subprocess.Popen("cd gui_scan/tomcat && " + java8_path + ' -jar ' + 'tomcat.jar', shell=True)

    def fastjson_cilck(self, event):
        subprocess.Popen("cd gui_scan/json && json反序列化检查工具.exe", shell=True)

    def cve_2020_10199_click(self, event):
        subprocess.Popen("cd gui_scan && " + java8_path + ' -jar ' + 'cve-2020-10199-10204.jar', shell=True)

    def cve_2019_7238_click(self, event):
        subprocess.Popen("cd gui_scan && " + java8_path + ' -jar ' + 'cve-2019-7238.jar', shell=True)

    def aliyun_accesskey_click(self, event):
        subprocess.Popen('cd gui_scan && Aliyun-.AK.Tools-V1.2.exe', shell=True)

    def aliyunakyools_click(self, event):
        subprocess.Popen('cd gui_scan/AliyunAkTools && AliyunAkTools.exe', shell=True)

    def jdgui_click(self, event):
        subprocess.Popen("cd gui_scan && " + java8_path + ' -jar ' + 'jd-gui-1.6.6.jar', shell=True)

    def mdut_click(self, event):
        subprocess.Popen("cd gui_scan/Multiple.Database.Utilization.Tools.-.v2.0.6 && " + java8_path + ' -jar ' + 'MDUT.jar', shell=True)

if __name__ == '__main__':
    app = wx.App()
    frame = MianWindow(None)
    frame.Show()
    app.MainLoop()

