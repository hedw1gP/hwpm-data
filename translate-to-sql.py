import json

# Those crazy albums are generated from Navicat. 
# It's a pity that Navicat cannot import JSON to seperate tables.
# If it can, then there is no this painful script.

def create_table_albums():
    sql = """
DROP TABLE IF EXISTS `character_albums`;
CREATE TABLE `character_albums`  (
    `Id` varchar(255) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL,
    `Name` varchar(255) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL,
    `HiraganaName` varchar(255) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL,
    `Skill1Id` varchar(255) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL,
    `Skill2Id` varchar(255) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL,
    `Skill3Id` varchar(255) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL,
    `SceneCount` varchar(255) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL,
    `ThumbnailImageIdentifier` varchar(255) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL,
    `VersionId` varchar(255) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL,
    `Type` varchar(255) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL,
    `CompleteRewardItemId` varchar(255) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL,
    `CompleteRewardItemCount` varchar(255) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL
) ENGINE = MyISAM CHARACTER SET = utf8 COLLATE = utf8_general_ci ROW_FORMAT = Dynamic;


"""
    return sql

def create_table_charactercards():
    sql = """DROP TABLE IF EXISTS `character_charactercards`;
CREATE TABLE `character_charactercards`  (
    `Id` varchar(255) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL,
    `CharacterId` varchar(255) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL,
    `Name` varchar(255) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL,
    `Description` varchar(255) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL,
    `Rarity` varchar(255) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL,
    `Type` varchar(255) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL,
    `TagIdBits` varchar(255) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL,
    `InitialTap` varchar(255) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL,
    `MaxTapRank1` varchar(255) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL,
    `MaxTapRank2` varchar(255) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL,
    `InitialTech` varchar(255) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL,
    `MaxTechRank1` varchar(255) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL,
    `MaxTechRank2` varchar(255) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL,
    `InitialKyunKyun` varchar(255) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL,
    `MaxKyunKyunRank1` varchar(255) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL,
    `MaxKyunKyunRank2` varchar(255) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL,
    `LevelCoefficientId` varchar(255) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL,
    `SkillId` varchar(255) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL,
    `CharacterCardRankUpItemSetId` varchar(255) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL,
    `FirstSceneCardId` varchar(255) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL,
    `RankUpSceneCardId` varchar(255) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL,
    `MusicPartId` varchar(255) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL,
    `CanUseSkillLevelUpItem` varchar(255) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL
) ENGINE = MyISAM CHARACTER SET = utf8 COLLATE = utf8_general_ci ROW_FORMAT = Dynamic;


"""
    return sql

def create_table_character_charactervoice():
    sql = """DROP TABLE IF EXISTS `character_charactervoice`;
CREATE TABLE `character_charactervoice`  (
    `Id` varchar(255) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL,
    `VoiceType` varchar(255) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL,
    `CharacterId` varchar(255) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL,
    `CharacterCardId` varchar(255) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL,
    `Rarity` varchar(255) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL,
    `Rank` varchar(255) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL,
    `TermId` varchar(255) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL,
    `SoundId` varchar(255) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL
) ENGINE = MyISAM CHARACTER SET = utf8 COLLATE = utf8_general_ci ROW_FORMAT = Dynamic;


"""
    return sql

def create_table_character_cooprations():
    sql = """DROP TABLE IF EXISTS `character_cooperations`;
CREATE TABLE `character_cooperations`  (
    `Id` varchar(255) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL,
    `Name` varchar(255) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL,
    `Description` varchar(255) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL,
    `MusicPartId` varchar(255) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL,
    `Rank` varchar(255) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL,
    `DisplayOrderPriority` varchar(255) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL,
    `SkillId` varchar(255) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL,
    `ClassId` varchar(255) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL,
    `Arg1` varchar(255) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL,
    `Arg2` varchar(255) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL,
    `Arg3` varchar(255) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL,
    `Arg4` varchar(255) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL,
    `Arg5` varchar(255) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL,
    `Arg6` varchar(255) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL,
    `Arg7` varchar(255) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL,
    `Arg8` varchar(255) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL,
    `Arg9` varchar(255) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL,
    `Arg10` varchar(255) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL
) ENGINE = MyISAM CHARACTER SET = utf8 COLLATE = utf8_general_ci ROW_FORMAT = Dynamic;


"""
    return sql;

def create_table_character_scenecards():
    sql = """DROP TABLE IF EXISTS `character_scenecards`;
CREATE TABLE `character_scenecards`  (
    `ItemId` varchar(255) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL,
    `Name` varchar(255) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL,
    `Description` varchar(255) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL,
    `AlbumId` varchar(255) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL,
    `DisplayOrderPriority` varchar(255) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL,
    `ImageIdentifier` varchar(255) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL,
    `StartAt` varchar(255) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL
) ENGINE = MyISAM CHARACTER SET = utf8 COLLATE = utf8_general_ci ROW_FORMAT = Dynamic;


"""
    return sql;

def create_table_character_tags():
    sql = """DROP TABLE IF EXISTS `character_tags`;
CREATE TABLE `character_tags`  (
    `Id` varchar(255) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL,
    `Name` varchar(255) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL,
    `NameKana` varchar(255) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL,
    `Description` varchar(255) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL,
    `IconLevel` varchar(255) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL,
    `VersionId` varchar(255) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL
) ENGINE = MyISAM CHARACTER SET = utf8 COLLATE = utf8_general_ci ROW_FORMAT = Dynamic;


"""
    return sql;

def create_table_character_version():
    sql = """DROP TABLE IF EXISTS `character_version`;
CREATE TABLE `character_version`  (
    `MasterVersion` bigint(20) NULL DEFAULT NULL,
    `CacheVersion` bigint(20) NULL DEFAULT NULL
) ENGINE = MyISAM CHARACTER SET = utf8 COLLATE = utf8_general_ci ROW_FORMAT = Fixed;


"""
    return sql;

def create_tables():
    sql = create_table_albums()+create_table_charactercards()+create_table_character_charactervoice()+create_table_character_cooprations()+create_table_character_scenecards()+create_table_character_tags()+create_table_character_version()
    return sql;


# Open Files
sql_file = open("hwpm_character.sql", "w", encoding="utf-8"); 
character_file = open("Character.json", "r", encoding="utf-8")
character_json = json.load(character_file)

# Write Drop-Create commands
sql_file.write(create_tables()) 

# Write Version
sql_file.write("INSERT INTO `character_version` VALUES ({}, {});".format(character_json["MasterVersion"], character_json["CacheVersion"]))
sql_file.write("\n\n")

# Albums parse
for line in character_json["Albums"]:
    sql_file.write("INSERT INTO `character_albums` VALUES ('{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}'); \n".format(line["Id"], line["Name"], line["HiraganaName"], line["Skill1Id"], line["Skill2Id"], line["Skill3Id"], line["SceneCount"], line["ThumbnailImageIdentifier"], line["VersionId"], line["Type"], line["CompleteRewardItemId"], line["CompleteRewardItemCount"]))

    # Wait, how there is None but still success?
    # That is what .format() for. I actually thought I have to replace
    # None to "None". But actually no need

sql_file.write("\n")
# CharacterCards parse
for line in character_json["CharacterCards"]:
    sql_file.write("INSERT INTO `character_charactercards` VALUES ('{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}'); \n".format(line["Id"], line["CharacterId"], line["Name"], line["Description"], line["Rarity"], line["Type"], line["TagIdBits"], line["InitialTap"], line["MaxTapRank1"], line["MaxTapRank2"], line["InitialTech"], line["MaxTechRank1"], line["MaxTechRank2"], line["InitialKyunKyun"], line["MaxKyunKyunRank1"], line["MaxKyunKyunRank2"], line["LevelCoefficientId"], line["SkillId"], line["CharacterCardRankUpItemSetId"], line["FirstSceneCardId"], line["RankUpSceneCardId"], line["MusicPartId"], line["CanUseSkillLevelUpItem"]))

sql_file.write("\n")

for line in character_json["Characters"]:
    sql_file.write("INSERT INTO `character_characters` VALUES ('{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}'); \n".format(line["Id"], line["Name"], line["HiraganaName"], line["VoiceActor"],line["Height"],line["Birthday"],line["Constellation"], line["BloodType"], line["Description"], line["ComboVoiceSoundId"], line["DefaultCharacterCardId"]))

sql_file.write("\n")

for i in character_json["CharacterTalk"]:
    sql_file.write("INSERT INTO `character_charactertalk` VALUES ('{}', '{}', '{}', '{}'); \n".format(i["Id"], i["Character1Id"], i["Character2Id"], i["VoiceId"]))

sql_file.write("\n")

for i in character_json["CharacterVoice"]:
    sql_file.write("INSERT INTO `character_charactervoice` VALUES ('{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}'); \n".format(i["Id"], i["VoiceType"], i["CharacterId"], i["CharacterCardId"], i["Rarity"], i["Rank"], i["TermId"], i["SoundId"]))

sql_file.write("\n")

for i in character_json["Cooperations"]:
    sql_file.write("INSERT INTO `character_cooperations` VALUES ('{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}'); \n".format(i["Id"], i["Name"], i["Description"], i["MusicPartId"],  i["Rank"],  i["DisplayOrderPriority"],  i["SkillId"],  i["ClassId"],  i["Arg1"],  i["Arg2"],  i["Arg3"],  i["Arg4"],  i["Arg5"],  i["Arg6"],  i["Arg7"],  i["Arg8"],  i["Arg9"],  i["Arg10"]))
    
sql_file.write("\n")

for i in character_json["SceneCards"]:
    sql_file.write("INSERT INTO `character_scenecards` VALUES ('{}', '{}', '{}', '{}', '{}', '{}', '{}'); \n".format(i["ItemId"], i["Name"], i["Description"], i["AlbumId"], i["DisplayOrderPriority"], i["ImageIdentifier"], i["StartAt"]))

sql_file.write("\n")

for i in character_json["Tags"]:
    sql_file.write("INSERT INTO `character_tags` VALUES ('{}', '{}', '{}', '{}', '{}', '{}'); \n".format(i["Id"], i["Name"], i["NameKana"], i["Description"], i["IconLevel"], i["VersionId"]))

sql_file.write("\n")