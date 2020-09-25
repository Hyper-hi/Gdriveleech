from tobrot.sample_config import Config
#Fill your all data, read readme for reference

class Config(Config):
	TG_BOT_TOKEN= "1243895049:AAEAMCBi-STQqjKzzpxjP5EEvV6WCl9XLFQ"
	APP_ID = 1314600
	API_HASH = "a9caac8a771a5e27f617f1822288d753"
	OWNER_ID = "693989702" #ID of bot owner
	AUTH_CHANNEL = [-1001128611435]
	DESTINATION_FOLDER = "Hyper" #Name of your folder read readme
	RCLONE_CONFIG = """type = drive\nscope = drive\ntoken = {"access_token":"ya29.a0AfH6SMCWzs9D4vZLS0fwbmCw8orDJneUvMwErTJiNjSA-jRSFNsoBab6YdFQ85Xs1Ajb1OL-irW8qNX4G_F-5i6Nk_7imdA99h5KXDVaHYtsMbRo_KHTMDGmdgNrc-YGpc16M2YPW8pmmIo_z9rCQJ4q1ggMA_XCfgg","token_type":"Bearer","refresh_token":"1//0g4wnAU2VEe4KCgYIARAAGBASNwF-L9Irh2q2b8tgCdm2IeMBJ_pQ6cWn4LZsiB0VHKW2EvA0n_ngpkYp7BDyl9WxA8lWXXXCYLk","expiry":"2020-07-22T12:42:42.6241114+05:30"}
team_drive = 0AKvqrGm6XBF_Uk9PVA"""
	#fill taking reference of this config, dont remove """ from both side of the RCLONE_CONFIG variable 
	INDEX_LINK = os.environ.get("INDEX_LINK", "http://a.mera.workers.dev")
