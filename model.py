import torch
import torch.nn as nn
import torch.nn.init as init

<<<<<<< HEAD
class rdcnn_2_larger(nn.Module):
    def __init__(self, drop_rate):
        super(rdcnn_2_larger, self).__init__()
        self.encoder  = nn.Sequential(
            nn.Conv2d(4, 84, 3, stride=2, padding=1),  # b, 84, 11, 11
            nn.BatchNorm2d(84),
            nn.ReLU(True),
            nn.Dropout(drop_rate) ,

            nn.Conv2d(84, 168, 3, stride=2, padding=1),  # b, 168, 6, 6
            nn.BatchNorm2d(168),
            nn.ReLU(True),
            nn.Dropout(drop_rate) ,

            nn.MaxPool2d(2, stride=1),  # b, 168, 5, 5
            nn.Conv2d(168, 336, 3, stride=2, padding=1),  # b, 336, 3, 3
            nn.BatchNorm2d(336),
            nn.ReLU(True),
            nn.Dropout(drop_rate) ,

            nn.MaxPool2d(2, stride=1),  # b, 336, 2, 2
            nn.Dropout(drop_rate) ,
        )
        self.decoder = nn.Sequential(
            nn.ConvTranspose2d(336, 672, 3, stride=2, padding=1),  # b, 672, 3, 3
            nn.BatchNorm2d(672),
            nn.ReLU(True),
            nn.ConvTranspose2d(672, 336, 2, stride=2),  # b, 336, 6, 6
            nn.BatchNorm2d(336),
            nn.ReLU(True),
            nn.ConvTranspose2d(336, 84, 2, stride=2),  # b, 84, 12, 12
            nn.BatchNorm2d(84),
            nn.ReLU(True),
            nn.ConvTranspose2d(84, 1, 3, stride=2,padding=2),  # b, 1, 21, 21
        )

    def forward(self, x):
        x = self.encoder(x)
        x = self.decoder(x)
        return x

=======
# For 4 channel Dataset
class rdcnn(nn.Module):
    def __init__(self, drop_rate):
        super(rdcnn, self).__init__()
        self.discriminator  = nn.Sequential(
            nn.Conv2d(4, 16, 3, stride=2, padding=0),  # b, 16, 10, 10
            nn.ReLU(True),
            nn.MaxPool2d(2, stride=2),  # b, 16, 5, 5
            nn.Conv2d(16, 8, 3, stride=2, padding=1),  # b, 8, 3, 3
            nn.ReLU(True),
            nn.MaxPool2d(2, stride=1)  # b, 8, 2, 2
        )
        self.generator = nn.Sequential(
            nn.ConvTranspose2d(8, 16, 3, stride=2),  # b, 16, 5, 5
            nn.ReLU(True),
            nn.ConvTranspose2d(16, 8, 2, stride=2),  # b, 8, 10, 10
            nn.ReLU(True),
            nn.ConvTranspose2d(8, 1, 3, stride=2),  # b, 1, 21, 21
            nn.Tanh()
        )
        self.dropout = nn.Dropout(drop_rate) 

    def forward(self, x):
        x = self.discriminator(x)
        x = self.generator(x)
        x = self.dropout(x)
        return x

# Old result with tanh
# class rdcnn_2(nn.Module):
#     def __init__(self, drop_rate):
#         super(rdcnn_2, self).__init__()
#         self.discriminator  = nn.Sequential(
#             nn.Conv2d(5, 40, 3, stride=2, padding=1),  # b, 40, 11, 11
#             nn.ReLU(True),
#             nn.Dropout(drop_rate) ,
#             nn.Conv2d(40, 20, 3, stride=2, padding=1),  # b, 20, 6, 6
#             nn.ReLU(True),
#             nn.Dropout(drop_rate) ,
#             nn.MaxPool2d(2, stride=1),  # b, 8, 5, 5
#             nn.Conv2d(20, 10, 3, stride=2, padding=1),  # b, 10, 3, 3
#             nn.ReLU(True),
#             nn.Dropout(drop_rate) ,
#             nn.MaxPool2d(2, stride=1),  # b, 10, 2, 2
#             nn.Dropout(drop_rate) ,
#         )
#         self.generator = nn.Sequential(
#             nn.ConvTranspose2d(10, 40, 3, stride=2, padding=1),  # b, 40, 3, 3
#             nn.ReLU(True),
#             nn.ConvTranspose2d(40, 20, 2, stride=2),  # b, 20, 6, 6
#             nn.ReLU(True),
#             nn.ConvTranspose2d(20, 10, 2, stride=2),  # b, 10, 12, 12
#             nn.Tanh(),
#             nn.ConvTranspose2d(10, 1, 3, stride=2,padding=2),  # b, 1, 21, 21
#             nn.Tanh()
#         )

#     def forward(self, x):
#         x = self.discriminator(x)
#         x = self.generator(x)
#         return x

# ReLU activation
class rdcnn_2(nn.Module):
    def __init__(self, drop_rate):
        super(rdcnn_2, self).__init__()
        self.discriminator  = nn.Sequential(
            nn.Conv2d(4, 40, 3, stride=2, padding=1),  # b, 40, 11, 11
            nn.ReLU(True),
            nn.Dropout(drop_rate) ,
            nn.Conv2d(40, 20, 3, stride=2, padding=1),  # b, 20, 6, 6
            nn.ReLU(True),
            nn.Dropout(drop_rate) ,
            nn.MaxPool2d(2, stride=1),  # b, 8, 5, 5
            nn.Conv2d(20, 10, 3, stride=2, padding=1),  # b, 10, 3, 3
            nn.ReLU(True),
            nn.Dropout(drop_rate) ,
            nn.MaxPool2d(2, stride=1),  # b, 10, 2, 2
            nn.Dropout(drop_rate) ,
        )
        self.generator = nn.Sequential(
            nn.ConvTranspose2d(10, 40, 3, stride=2, padding=1),  # b, 40, 3, 3
            nn.ReLU(True),
            nn.ConvTranspose2d(40, 20, 2, stride=2),  # b, 20, 6, 6
            nn.ReLU(True),
            nn.ConvTranspose2d(20, 10, 2, stride=2),  # b, 10, 12, 12
            nn.ReLU(True),
            nn.ConvTranspose2d(10, 1, 3, stride=2,padding=2),  # b, 1, 21, 21
            nn.ReLU(True)
        )

    def forward(self, x):
        x = self.discriminator(x)
        x = self.generator(x)
        return x

# ELU activation
class rdcnn_3(nn.Module):
    def __init__(self, drop_rate):
        super(rdcnn_3, self).__init__()
        self.discriminator  = nn.Sequential(
            nn.Conv2d(4, 40, 3, stride=2, padding=1),  # b, 40, 11, 11
            nn.ELU(True),
            nn.Dropout(drop_rate) ,
            nn.Conv2d(40, 20, 3, stride=2, padding=1),  # b, 20, 6, 6
            nn.ELU(True),
            nn.Dropout(drop_rate) ,
            nn.MaxPool2d(2, stride=1),  # b, 8, 5, 5
            nn.Conv2d(20, 10, 3, stride=2, padding=1),  # b, 10, 3, 3
            nn.ELU(True),
            nn.Dropout(drop_rate) ,
            nn.MaxPool2d(2, stride=1),  # b, 10, 2, 2
            nn.Dropout(drop_rate) ,
        )
        self.generator = nn.Sequential(
            nn.ConvTranspose2d(10, 40, 3, stride=2, padding=1),  # b, 40, 3, 3
            nn.ELU(True),
            nn.ConvTranspose2d(40, 20, 2, stride=2),  # b, 20, 6, 6
            nn.ELU(True),
            nn.ConvTranspose2d(20, 10, 2, stride=2),  # b, 10, 12, 12
            nn.ELU(True),
            nn.ConvTranspose2d(10, 1, 3, stride=2,padding=2),  # b, 1, 21, 21
            nn.ELU(True),
        )

    def forward(self, x):
        x = self.discriminator(x)
        x = self.generator(x)
        return x

# PReLU activation
class rdcnn_4(nn.Module): 
    def __init__(self, drop_rate):
        super(rdcnn_4, self).__init__()
        self.discriminator  = nn.Sequential(
            nn.Conv2d(4, 40, 3, stride=2, padding=1),  # b, 40, 11, 11
            nn.PReLU(),
            nn.Dropout(drop_rate) ,
            nn.Conv2d(40, 20, 3, stride=2, padding=1),  # b, 20, 6, 6
            nn.PReLU(),
            nn.Dropout(drop_rate) ,
            nn.MaxPool2d(2, stride=1),  # b, 8, 5, 5
            nn.Conv2d(20, 10, 3, stride=2, padding=1),  # b, 10, 3, 3
            nn.PReLU(),
            nn.Dropout(drop_rate) ,
            nn.MaxPool2d(2, stride=1),  # b, 10, 2, 2
            nn.Dropout(drop_rate) ,
        )
        self.generator = nn.Sequential(
            nn.ConvTranspose2d(10, 40, 3, stride=2, padding=1),  # b, 40, 3, 3
            nn.PReLU(),
            nn.ConvTranspose2d(40, 20, 2, stride=2),  # b, 20, 6, 6
            nn.PReLU(),
            nn.ConvTranspose2d(20, 10, 2, stride=2),  # b, 10, 12, 12
            nn.PReLU(),
            nn.ConvTranspose2d(10, 1, 3, stride=2,padding=2),  # b, 1, 21, 21
            nn.PReLU(),
        )

    def forward(self, x):
        x = self.discriminator(x)
        x = self.generator(x)
        return x
>>>>>>> e3866c46f4ea3e48390a009cf47add22fe43551a
