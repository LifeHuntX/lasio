# TODO: Replace all these classes as inheriting a parent class from spec_stubs.py
#
# If the class checks off on a specification, it should inherit from the
# stub class for that specification.
#
# Please do not create a child of multiple specifications. We want the
# functionality to be granular - remember we want these classes to also 
# implement a "correct()" method in the future, which will be more difficult
# to implement if they inherit from multiple specifications.
from spec_stubs import *


class WellSectionExists_V12(Requirement_f5b59a3f_V12):
    @staticmethod
    def check(las_file):
        return "Well" in las_file.sections


class WellSectionExists_V20(Requirement_f0cf897f_V20):
    @staticmethod
    def check(las_file):
        return "Well" in las_file.sections


# class VersionSectionExists(Rule):
#     @staticmethod
#     def check(las_file):
#         return "Version" in las_file.sections


# class CurvesSectionExists(Rule):
#     @staticmethod
#     def check(las_file):
#         return "Curves" in las_file.sections


# class AsciiSectionExists(Rule):
#     @staticmethod
#     def check(las_file):
#         if "Curves" in las_file.sections:
#             for curve in las_file.curves:
#                 if len(curve.data) == 0:
#                     return False
#             return True
#         else:
#             return False


# class MandatoryLinesInVersionSection(Rule):
#     @staticmethod
#     def check(las_file):
#         if "Version" in las_file.sections:
#             mandatory_lines = ["VERS", "WRAP"]
#             return all(elem in las_file.version for elem in mandatory_lines)
#         return False


# class MandatoryLinesInWellSection(Rule):
#     @staticmethod
#     def check(las_file):
#         if "Well" in las_file.sections:
#             # PROV, UWI can have alternatives
#             mandatory_lines = ["STRT", "STOP", "STEP", "NULL", "COMP", "WELL", "FLD", "LOC", "SRVC", "DATE"]
#             mandatory_sections_found = all(elem in las_file.well for elem in mandatory_lines)
#             if not mandatory_sections_found:
#                 return False
#             if "UWI" not in las_file.well and "API" not in las_file.well:
#                 return False
#             if "PROV" not in las_file.well and \
#                "CNTY" not in las_file.well and \
#                "CTRY" not in las_file.well and \
#                "STAT" not in las_file.well:
#                 return False
#             return True
#         return False


# class DuplicateSections(Rule):
#     @staticmethod
#     def check(las_file):
#         if las_file.duplicate_v_section or \
#                 las_file.duplicate_w_section or \
#                 las_file.duplicate_p_section or \
#                 las_file.duplicate_c_section or \
#                 las_file.duplicate_o_section or \
#                 las_file.sections_after_a_section:
#             return False
#         else:
#             return True


# class ValidIndexMnemonic(Rule):
#     @staticmethod
#     def check(las_file):
#         if las_file.curves[0].mnemonic == "DEPT" or \
#                 las_file.curves[0].mnemonic == "DEPTH" or \
#                 las_file.curves[0].mnemonic == "TIME" or \
#                 las_file.curves[0].mnemonic == "INDEX":
#             return True
#         return False


# class ValidDepthDividedByStep(Rule):
#     @staticmethod
#     def check(las_file):
#         if las_file.curves[0].mnemonic != "DEPT" and \
#                 las_file.curves[0].mnemonic != "DEPTH":
#             return True
#         else:
#             index_data =las_file[las_file.curves[0].mnemonic]
#             for dept_value in index_data:
#                 if dept_value % las_file.well.step.value != 0:
#                     return False
#             return True


# class VSectionFirst(Rule):
#     @staticmethod
#     def check(las_file):
#         return las_file.v_section_first