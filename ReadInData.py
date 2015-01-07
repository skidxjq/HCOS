# -*- coding: utf-8 -*-
import csv


def covertMetadataToArr(filePath):
    # todo use thread
    csvDict = {}
    with open(filePath, 'r') as f:
        rd = csv.reader(f)
        for r in rd:  # for every line in the csv file
            eachLine = ','.join(r)
            eachLineArray = eachLine.split(',')  # put the content of each line into an array
            tmpStr = eachLineArray[1]
            if tmpStr == '人员要素':
                if 'people' in csvDict:
                    csvDict['people'] = dict(csvDict['people'],
                                             **{eachLineArray[2]: {'表内序号': eachLineArray[0], '字段名称': eachLineArray[3],
                                                                   '字段描述': eachLineArray[4], '字段类型': eachLineArray[5],
                                                                   '长度': eachLineArray[6], '内部标识符': eachLineArray[7],
                                                                   '中文名称': eachLineArray[8], '标识符': eachLineArray[9],
                                                                   '数据类型': eachLineArray[10],
                                                                   '表示格式': eachLineArray[11]}})
                else:
                    csvDict['people'] = {eachLineArray[2]: {'表内序号': eachLineArray[0], '字段名称': eachLineArray[3],
                                                            '字段描述': eachLineArray[4], '字段类型': eachLineArray[5],
                                                            '长度': eachLineArray[6], '内部标识符': eachLineArray[7],
                                                            '中文名称': eachLineArray[8], '标识符': eachLineArray[9],
                                                            '数据类型': eachLineArray[10],
                                                            '表示格式': eachLineArray[11]}}
            elif tmpStr == '物品要素':
                if 'items' in csvDict:
                    csvDict['items'] = dict(csvDict['items'],
                                            **{eachLineArray[2]: {'表内序号': eachLineArray[0], '字段名称': eachLineArray[3],
                                                                  '字段描述': eachLineArray[4], '字段类型': eachLineArray[5],
                                                                  '长度': eachLineArray[6], '内部标识符': eachLineArray[7],
                                                                  '中文名称': eachLineArray[8], '标识符': eachLineArray[9],
                                                                  '数据类型': eachLineArray[10],
                                                                  '表示格式': eachLineArray[11]}})
                else:
                    csvDict['items'] = {eachLineArray[2]: {'表内序号': eachLineArray[0], '字段名称': eachLineArray[3],
                                                           '字段描述': eachLineArray[4], '字段类型': eachLineArray[5],
                                                           '长度': eachLineArray[6], '内部标识符': eachLineArray[7],
                                                           '中文名称': eachLineArray[8], '标识符': eachLineArray[9],
                                                           '数据类型': eachLineArray[10],
                                                           '表示格式': eachLineArray[11]}}
            elif tmpStr == '机构要素':
                if 'orgs' in csvDict:
                    csvDict['orgs'] = dict(csvDict['orgs'],
                                           **{eachLineArray[2]: {'表内序号': eachLineArray[0], '字段名称': eachLineArray[3],
                                                                 '字段描述': eachLineArray[4], '字段类型': eachLineArray[5],
                                                                 '长度': eachLineArray[6], '内部标识符': eachLineArray[7],
                                                                 '中文名称': eachLineArray[8], '标识符': eachLineArray[9],
                                                                 '数据类型': eachLineArray[10],
                                                                 '表示格式': eachLineArray[11]}})
                else:
                    csvDict['orgs'] = {eachLineArray[2]: {'表内序号': eachLineArray[0], '字段名称': eachLineArray[3],
                                                          '字段描述': eachLineArray[4], '字段类型': eachLineArray[5],
                                                          '长度': eachLineArray[6], '内部标识符': eachLineArray[7],
                                                          '中文名称': eachLineArray[8], '标识符': eachLineArray[9],
                                                          '数据类型': eachLineArray[10],
                                                          '表示格式': eachLineArray[11]}}
            elif tmpStr == '案(事)件要素':
                if 'events' in csvDict:
                    csvDict['events'] = dict(csvDict['events'],
                                             **{eachLineArray[2]: {'表内序号': eachLineArray[0], '字段名称': eachLineArray[3],
                                                                   '字段描述': eachLineArray[4], '字段类型': eachLineArray[5],
                                                                   '长度': eachLineArray[6], '内部标识符': eachLineArray[7],
                                                                   '中文名称': eachLineArray[8], '标识符': eachLineArray[9],
                                                                   '数据类型': eachLineArray[10],
                                                                   '表示格式': eachLineArray[11]}})
                else:
                    csvDict['events'] = {eachLineArray[2]: {'表内序号': eachLineArray[0], '字段名称': eachLineArray[3],
                                                            '字段描述': eachLineArray[4], '字段类型': eachLineArray[5],
                                                            '长度': eachLineArray[6], '内部标识符': eachLineArray[7],
                                                            '中文名称': eachLineArray[8], '标识符': eachLineArray[9],
                                                            '数据类型': eachLineArray[10],
                                                            '表示格式': eachLineArray[11]}}
            elif tmpStr == '地点要素':
                if 'locations' in csvDict:
                    csvDict['locations'] = dict(csvDict['locations'],
                                                **{
                                                    eachLineArray[2]: {'表内序号': eachLineArray[0],
                                                                       '字段名称': eachLineArray[3],
                                                                       '字段描述': eachLineArray[4],
                                                                       '字段类型': eachLineArray[5],
                                                                       '长度': eachLineArray[6],
                                                                       '内部标识符': eachLineArray[7],
                                                                       '中文名称': eachLineArray[8],
                                                                       '标识符': eachLineArray[9],
                                                                       '数据类型': eachLineArray[10],
                                                                       '表示格式': eachLineArray[11]}})
                else:
                    csvDict['locations'] = {eachLineArray[2]: {'表内序号': eachLineArray[0], '字段名称': eachLineArray[3],
                                                               '字段描述': eachLineArray[4], '字段类型': eachLineArray[5],
                                                               '长度': eachLineArray[6], '内部标识符': eachLineArray[7],
                                                               '中文名称': eachLineArray[8], '标识符': eachLineArray[9],
                                                               '数据类型': eachLineArray[10],
                                                               '表示格式': eachLineArray[11]}}
            else:
                pass
    return csvDict


if __name__ == '__main__':
    testDict = covertMetadataToArr('gongan.csv')
    # print testDict
    aaa = testDict['people']['CRJ_CCRJZJRYXX']
    for key in aaa.keys():
        print key + '\t',
        print aaa[key]