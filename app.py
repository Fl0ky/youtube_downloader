

from kivymd.app import MDApp
from kivymd.uix.screen import MDScreen
from kivymd.uix.toolbar import MDToolbar
from kivymd.uix.textfield import MDTextField
from kivymd.uix.button import MDFillRoundFlatButton
from pytube import YouTube


class YTDApp(MDApp):

    def download_video(self, url):
        val=self.input.text
        yt = YouTube(val)
        return yt.streams.filter(progressive=True, file_extension='mp4').order_by('resolution').desc().first().download('./')

    
    def build(self):
        screen = MDScreen()
        self.toolbar = MDToolbar(title='Youtube Downloader')
        self.toolbar.pos_hint = {'top': 1}
        screen.add_widget(self.toolbar)
        ### collect user input ###
        self.input = MDTextField(
            text='Enter the url of the video to be downloaded',
            halign = 'center',
            size_hint = (1, 0.1),
            pos_hint = {'center_x': 0.5, 'center_y': 0.5},
            
        )
        screen.add_widget(self.input)
        ### button ###
        screen.add_widget(MDFillRoundFlatButton(
            text='Download',
            font_size = 17,
            pos_hint={'center_x': 0.5, 'center_y': 0.3},
            on_release=self.download_video,
            
        ))

        return screen


if __name__ == "__main__":
    YTDApp().run()