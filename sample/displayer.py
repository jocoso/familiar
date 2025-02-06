import wx

class Displayer(wx.App):
    def __init__(self, image):
        self.image = image 
        super().__init__(useBestVisual=True, clearSigInt=True)

    def OnInit(self):
        self.frame = wx.Frame(parent=None, title="Familiar")
        self.draw(self.image)
        self.frame.Show()
        return True

    def draw(self, image):
        if self.frame and image:
            #img = wx.Image(image, wx.BITMAP_TYPE_ANY)
            #bitmap = wx.Bitmap(img)
            #wx.StaticBitmap(self.frame, -1, bitmap)
            #self.frame.SetClientSize(bitmap.getWidth(), bitmap.GetHeight())
            pass
