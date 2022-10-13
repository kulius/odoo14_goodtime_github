# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

from odoo import api, fields, models, _

class MachineLocaction(models.Model):
    _name = "machine.locaction"
    _description = "場域資訊"

    country_id = fields.Many2one(
        'res.country', '國家', tracking=True, default=227, invisible=True)
    state_id = fields.Many2one("res.country.state", string='縣市', domain="[('country_id', '=?', country_id)]")
    city_id = fields.Many2one('res.city', string='鄉鎮市區', domain="[('state_id', '=', state_id)]")
    area_address = fields.Char(string='地址')
    area_name = fields.Char(string='場域名稱', required=True)
    employee_area = fields.Many2many('hr.employee', string='場域負責人', required=True)
    area_rent = fields.Integer(string='租金')
    area_water_expense = fields.Integer(string='水費')
    area_electricity_expense = fields.Integer(string='電費')
    pay_way = fields.Selection(string='結帳方式',
        selection=[
            ("month", "月結"),
            ("half_year", "半年期"),
        ]
    )
    date_start = fields.Date(string='起始日')
    date_end = fields.Date(string='結束日')
    active = fields.Boolean(string='開啟', default=True)
    project_name = fields.Char(string='專案名稱')
    project_number = fields.Char(string='專案編號')

    def name_get(self):
        result = []
        for record in self:
            name = "%s %s %s %s" % (record.state_id.name,record.city_id.name,record.area_name,record.project_number)
            result.append((record.id, name))
        return result

class MachineList(models.Model):
    _name = "machine.list"
    _description = "機器清單"

    machine_name = fields.Char(string='機器名稱', required=True)
    active = fields.Boolean(string='開啟', default=True)
    area = fields.Many2one('machine.locaction', string='場域名稱', required=True,)
    vendor = fields.Many2many('res.partner', string='供應商', relation='rel_respartner_machine_list')
    machine_belong = fields.Char(string='機台所屬')
    customer = fields.Char(string='客戶名稱')
    operator = fields.Char(string='營運商')
    sales_category = fields.Char(string='銷售別')
    machine_category = fields.Char(string='機型')
    vmc = fields.Char(string='VMC', required=True)
    machine_number = fields.Char(string='機器號碼-主')
    machine_category1_number = fields.Char(string='機器號碼-副1')
    machine_category2_number = fields.Char(string='機器號碼-副2')
    machine_category3_number = fields.Char(string='機器號碼-副3')
    other_device1 = fields.Char(string='其他設備1')
    other_device2 = fields.Char(string='其他設備2')
    machine_responsible = fields.Many2one('res.partner', string='機台負責人')
    machine_start_date = fields.Date(string='出機日期')
    system_model = fields.Char(string='系統型號')
    contract_start = fields.Date(string='合約起始日')
    contract_end = fields.Date(string='合約終止日')
    machine_cost = fields.Integer(string='價格/月租金')
    machine_voltage = fields.Char(string='電壓')
    move_record = fields.Char(string='移動紀錄')
    machine_internet = fields.Char(string='網路')
    machine_sim = fields.Char(string='SIM卡/設備編碼')
    easy_card = fields.Char(string='悠遊卡機身')
    cellphone_pay = fields.Char(string='手機支付匯款帳號')
    key_number1 = fields.Char(string='鑰鎖號碼1')
    key_number2 = fields.Char(string='鑰鎖號碼2')
    key_number3 = fields.Char(string='鑰鎖號碼3')
    key_number4 = fields.Char(string='鑰鎖號碼4')
    key_count = fields.Char(string='鑰鎖數量')
    computer = fields.Char(string='電腦')
    operate_business_name = fields.Char(string='運營商號 天來網頁板')
    catch_psw1 = fields.Char(string='捕貨密碼1')
    catch_psw2 = fields.Char(string='捕貨密碼2')
    teamviewer = fields.Char(string='TeamViewer(ID)')
    teamviewer_pwd = fields.Char(string='TeamViewer(p@ssw0rd)')
    anydesk = fields.Char(string='AnyDesk(ID)')
    anydesk_pwd = fields.Char(string='AnyDesk(p@ssw0rd)')
    remote_pw = fields.Char(string='遠端PW')
    paper_wire = fields.Char(string='紙鈔機線')
    backstage = fields.Char(string='後臺編碼', groups='goodtime_udm.can_see_token')
    token = fields.Char(string='Token', groups='goodtime_udm.can_see_token')
    order_store =fields.Char(string='供應商號', groups='goodtime_udm.can_see_token')
    light = fields.Char(string='燈箱')
    note = fields.Char(string='備註')
    resume_change = fields.Char(string='更變履歷')

    def name_get(self):
        result = []
        for record in self:
            name = "%s(%s)" % (record.machine_name, record.vmc)
            result.append((record.id, name))
        return result

    # @api.model
    # def create(self, vals):
    #     new = super(MachineList, self).create(vals)
    #     if not self.machine_number:
    #         name = "%s" % (self.area.display_name)
    #     else:
    #         name = "%s %s" % (self.area.display_name, self.machine_number)
    #     tmp = self.env['res.partner'].search([('name', '=', name)])
    #     if not tmp:
    #         if self.area.area_address == False:
    #             street = self.name_get()
    #         else:
    #             street = self.area.area_address
    #         self.env['res.partner'].create({
    #             'name': name,
    #             'street': street,
    #         })
    #     return new
