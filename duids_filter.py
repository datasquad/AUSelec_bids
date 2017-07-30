# -*- coding: utf-8 -*-
"""
Created on Mon Feb  2 23:57:03 2015

@author: kpetruskevicius
"""
import os 
import csv
generator_list = csv.reader(open("generators_list.CSV", "rb"), delimiter=',')
region = ['SA1', 'VIC1', 'NSW1', 'QLD1', 'TAS1', 'ACT1']
dispatch_type = [ 'Network Service Provider', 'Generator', 'Generator ', 'Load Norm Off','']
category = ['Market', 'Non-Market', '']
classification = [ 'Non-Scheduled', 'Scheduled', 'Semi-Scheduled', '']
fuel_source_primary = [ 'Fossil', 'Renewable/ Biomass / Waste', 'Hydro', 'Fuel Oil', '', 'Wind', 'Biomass', 'Renewable', 'Solar', 'Landfill, Biogas', 'Landfill / Biogas', '']
fuel_source_descriptor = [ 'Diesel', 'Brown Coal', 'Coal Seam Methane', 'Landfill Methane / Landfill Gas', 'Natural Gas', 'Water', '', 'Black Coal', 'Wind', 'Bagasse', 'Landfill Gas', 'Solar PV', 'Waste Coal Mine Gas', 'Natural Gas / Diesel', 'Kerosene', 'Landfill, Biogas', 'Hydro', 'Coal Tailings', 'Sewerage/Waste Water', 'Macadamia Nut Shells', 'Natural Gas / Fuel Oil', 'Landfill / Biogas', '']
technology_type_primary = [ 'Combustion', '', 'Renewable', 'Wind', '']
technology_type_descriptor = [ 'Compression Reciprocating Engine', 'Steam Sub-Critical', 'Spark Ignition Reciprocating Engine', '', 'Open Cycle Gas turbines (OCGT)', 'Hydro - Gravity', 'Combined Cycle Gas Turbine (CCGT)', 'Run of River', 'Wind - Onshore', 'Steam - sub critical', 'Spark Ignition', 'Steam Super Critical', 'PV - Panels', 'Landfill, Biogas', 'Photovoltaic Flat Panel', 'Closed Cycle Gas Turbines (CCGT)', 'Steam - Super heated', 'Hydro - pump storage', '']
physical_unit_no = [ '1-3', '1-18', '1-12', '1', '1-54', '2', '1-2', '3', '4', 'B 1-2', 'KV 3-4', '1-5', '31', '36', ' B 1-2', ' M1-6', '5', '6', '7', '1-7', '2-3', '4-5', '3-4', '1-23', '1-67', 'C 1-2', 'L 1-3', 'W 1-3', '1-33', '1-35', '1-11', '1-27', '1-14', '1-15', '0', '1-8', '1-4', '2b', '17-20', '1-16', '18-73', '1-17.', '1-31', '1-45', '1-34', '5-6', '7-10', '11-12', '8', '1-53', '1-13', '1-46', 'L 1', 'W 1', '1-6', '12-15', '1-140', '1-21', '11', '12', '1-64', '1-10', '1-56', '1-63', '32', '15-16', '3-6', '19-36', '1-74', '1-20', '1-42', '1-48', '1-47', '1-25', '1-40', '5-8', '1-37', '1-55', '1-128', 'WBP 1-37', 'WSB 1-25', '']
unit_size = [ '1.34', '1.667', '165', '1.03', '1.123', '47', '1.02', '5.3', '2.25', '0.8', '37', '30', '478', '594', '79.9', '660', '35', '40', '80', '1.44', '70', '1', '52', '61', '25', '173', '168', '8', '0.65', '1.15', '0.5', '0.75', '4.2', '1.9', '19', '5.7', '15.4', '14.4', '350', '420', '2', '0.013', '0.011', '0.168', '24', '27.9', '12.8', '85', '1.5', '14.5', '17', '1.3', '181', '43', '57', '3', '280', '121', '150', '60', '1.35', '4.5', '7.5', '33', '75', '720', '41.5', '43.2', '3.3', '5.8', '3.8', '1.08', '144', '1.26', '2.5', '2.1', '16.8', '25.2', '17.9', '200', '2.05', '29', '1.8', '38.8', '9', '51', '76', '1.1', '14', '21', '18', '7', '6', '1.064', '744', '39', '1.75', '32.4', '156', '30.6', '500', '1.125', '560', '530', '4.6', '426', '90', '1.57', '3.02', '0.77', '283', '700', '146', '131', '95', '138', '1.06', '265', '141', '1.037', '118', '62', '28', '160', '158', '6.7', '30.86', '36.92', '50', '23.5', '1.6', '128', '3.5', '38', '115.6', '0.7', '10.5', '13.55', '0.25', '1.05', '1.48', '365', '385', '460', '68', '58', '450', '15', '120', '82', '20', '82.8', '72', '250', '166', '5', '1.65', '0.715', '0.275', '31', '1.67 (average)', '0.6', '240', '4.7', '1.065', '4', '360', '380', '4.725', '154', '']
aggregation = [ 'N', 'Y', '']
reg_cap = [ '4', '30', '20', '165', '55.6', '1.123', '47', '3', '12.85', '-', '2', '37', '478', '594', '79.9', '660', '35', '240', '', '7.2', '70', '1', '52', '61', '300', '173', '168', '5', '38', '50', '2.83', '4.95', '2.18', '19', '27', '14.4', '350', '420', '46', '140', '170.1', '66', '85', '52.5', '11', '57', '17', '18.2', '181', '144', '24', '33', '644', '_', '150', '60', '8.984', '5.4', '90', '75', '720', '41.5', '43.2', '13.2', '32', '280', '5.8', '13', '432', '1.26', ' - ', '166', '94.5', '71.4', '180', '200', '4.1', '29', '25', '2.3', '51', '76', '1.1', '14', '21', '18', '7', '6', '1.064', '744', '40', '159', '39', '80.5', '32.4', '312', '81.6', '500', '31', '560', '530', '426', '12.56', '63', '283', '131', '700', '146', '1500', '3.2', '132.3', '265', '141', '67', '28', '6.7', '30.86', '36.92', '100', '23.5', '28.8', '148', '128', '3.5', '115.6', '10.5', '13.55', '160', '126', '99', '0.25', '4.2', '365', '34.5', '1.5', '385', '460', '208', '58', '10', '443', '15', '0.5', '2.5', '120', '41.2', '82', '80', '82.8', '616', '125', '111', '90.75', '192', '12', '250', '4.7', '6.738', '48', '360', '380', '9', '154', '']
max_cap = [ '4', '30', '20', '165', '55', '1', '47', '3', '13', '-', '2', '37', '33', '478', '594', '88', '700', '49', '240', '7', '80', '52', '61', '300', '173', '5', '38', '50', '', '2.83', '6', '2.18', '19', '28', '15', '385', '500', '46', '140', '183', '66', '100', '53', '11', '57', '18', '181', '144', '24', '663', '185', '65', '10', '60', '90', '75', '750', '56', '45', '285', '450', '1.26', ' - ', '172', '9', '95', '71', '220', '4.1', '70', '29', '51', '25', '2.3', '14', '22', '8', '781', '159', '39', '81', '34', '346', '86', '550', '31.8', '590', '535', '580', '600', '420', '89', '42', '105', '281', '131', '152', '139', '1575', '168', '510', '132', '273', '171', '63', '204', '68', '252', '124', '248', '23', '32', '148', '128', '48', '151', '119', '175', '126', '99', '69', '170', '4.2', '35', '460', '208', '58', '480', '94', '52.5', '21', '120', '210', '41', '174', '84', '103', '92', '665', '1800', '166', '680', '390', '111', '91', '192', '31', '12', '312', '245', '395', '380', '405', '180', '']
max_roc_min = [ '17', '4', '3', '200', '40', '140', '10', '25', '201', '60', '35', '43', '6', '77', '100', '110', '12', '34', '29', '0', '133', '20', '18', '15', '30', '57', '180', ' - ', '47', '44', '2', '23', '5', '157', '32', '118', '108', '116', '840', '16', '90', '13', '33', '31', '28', '450', '7', '41', '26', '9', '50', '92', '96', '320', '600', '75', '120', '49', '79', '76', '81', '36', '']
DUID_13 =[] 
gen=[]

generator_list = csv.reader(open("generators_list.CSV", "rb"), delimiter=',')
for i in generator_list:
    if i[2] in region:
        if i[3] in dispatch_type:
            if i[4] in category:
                if i[5] in classification:
                    if i[6] in fuel_source_primary:
                        if i[7] in fuel_source_descriptor:
                            if i[8] in technology_type_primary:
                                if i[9] in technology_type_descriptor:
                                    if i[10] in physical_unit_no:
                                        if i[11] in unit_size:
                                            if i[12] in aggregation:
                                                if i[14] in reg_cap:
                                                    if i[15] in max_cap:
                                                        if i[16] in max_roc_min:
                                                            DUID_13.append(i[13])
                                                                                             
print DUID_13