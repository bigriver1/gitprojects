# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

from scrapy.item import Item, Field


class GuluItem(Item):
##########第一级数据###############
    # 子类的url
    detail_url = Field()
    # 类型 0雷达、1车、2房、3保险、4生活、5教育、6移民、7头条
    type = Field()
    # 所在城市
    # city = Field()
    # 标题
    title = Field()
    # 内容
    # content = Field()
    # 图片url
    image_url = Field()
    # 标签
    tag = Field()

#########第二级数据############
    # 地址
    # address = Field()

    #网站相关链接
    # link_url = Field()
    # 详情
    content_text = Field()

    # 添加时间
    addtime = Field()

    # 详情大图
    detail_img = Field()

    # 更新时间
    update_time = Field()


    # # 布尔值，确认是否已爬取
    # python_bool = Field()



    # define the fields for your item here like:
    # name = scrapy.Field()
    # pass