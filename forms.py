from django import forms

entry = [
    ('rejected freight', 'rejected freight'),
    ('fleet owner', 'fleet owner'),
    ('freight', 'freight'),
    ('cargo', 'cargo'),
    ('freight capacity', 'freight capacity'),
    ('spot prices', 'spot prices'),
    ('electronic logistics marketplace', 'electronic logistics marketplace'),
    ('load posting', 'load posting'),
    ('freight intelligence', 'freight intelligence'),
    ('haulage company', 'haulage company'),
    ('freight exchange', 'freight exchange'),
    ('freight procurement', 'freight procurement'), 

    ('cargo documentation', 'cargo documentation'),
    ('freight tender', 'freight tender'),
    ('shipping lead time', 'shipping lead time'),
    ('multimodal freight', 'multimodal freight'),
    ('shipping estimate', 'shipping estimate'),
    ('freight as a service (FaaS)', 'freight as a service (FaaS)'),
    ('palletization', 'palletization'),
    ('freight quote', 'freight quote'),
    ('freight rate', 'freight rate'),
    ('shipment tracking', 'shipment tracking'),

    ('last mile delivery', 'last mile delivery'),
    ('freight forwarder', 'freight forwarder'),
    ('capacity sourcing', 'capacity sourcing'),
    ('autonomous trucking', 'autonomous trucking'),
    ('telematics', 'telematics'),
    ('digital freight matching', 'digital freight matching'),
    ('load board', 'load board'),
    ('freight broker', 'freight broker'),
    ('owner operator', 'owner operator'),
    ('semi-truck', 'semi-truck'),

    ('long-haul trucking', 'long-haul trucking'),
    ('heavy loads', 'heavy loads'),
    ('bulk liquid cargo', 'bulk liquid cargo'),
    ('bulk dry cargo', 'bulk dry cargo'),
    ('less-than-truckload (LTL)', 'less-than-truckload (LTL)'),
    ('full truckload (FTL)', 'full truckload (FTL)'),
    ('in-House Trucking', 'in-House Trucking'),
    ('less than container load', 'less than container load'),
    ('full container load', 'full container load'),
    ('freight matching', 'freight matching'),

    ('bill of lading', 'bill of lading'),
    ('load matching', 'load matching'),
    ('third party logistics', 'third party logistics'),
    ('flatbed trailer', 'flatbed trailer'),
    ('transportation management system', 'transportation management system'),
    ('hazmat', 'hazmat'),
    ('mixed load', 'mixed load'),
    ('consignee', 'consignee'),
    ('consignment', 'consignment'),
    ('consignor', 'consignor'),

    ('backhaul', 'backhaul'),
    ('tl market', 'tl market'),
    ('dat', 'dat'),
    ('equipment', 'equipment'),
    ('load planner', 'load planner'),
    ('tendering', 'tendering'),
    ('load shipment', 'load shipment'),
    ('conveyance', 'conveyance'),
    ('deadhead', 'deadhead'),
    ('empty mile', 'empty mile'),

    ('drop and hook', 'drop and hook'),
    ('unloading point', 'unloading point'),
    ('shipment', 'shipment'),
    ('carrier', 'carrier'),
    ('shipper', 'shipper'),
    ('loading', 'loading'),
    
]

class MainForm(forms.Form):
    query = forms.CharField(label=False, max_length=50, widget=forms.TextInput(attrs={'placeholder': 'اینجا جستجو کنید...'}), error_messages={
        'required': 'واژه مورد نظر را وارد کنید'
    })
    
class FeedForm(forms.Form):
    feedbox = forms.CharField(label='معنی پیشنهادی‌تان را بنویسید', max_length=80, widget=forms.Textarea)

class WordSel(forms.Form):
    wordchoice = forms.CharField(label='واژه انتخابی', widget=forms.Select(choices=entry, attrs={'id': 'word-select'}))
    comment = forms.CharField(label='نظر شما', widget=forms.Textarea, max_length=100)

    #def __init__(self, *args, **kwargs):
    #    super(MainForm, self).__init__(*args, **kwargs)
    #    self.fields['query'].widget.attrs.update({'class': ''})


