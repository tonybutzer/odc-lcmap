/* this is a multi
comment */

provider "aws" {
  region = "${var.region}"
}


resource "aws_instance" "odc1" {

  ami           = "${var.ami}"

  instance_type = "${var.instance_type}"
  key_name                    = "${var.key_name}"
  tags {
    Name = "odc1"
    Owner = "tonybutzer@gmail.com"
  }
  iam_instance_profile                    ="${var.iam_role}"
  security_groups = ["${var.security_group}"]
  user_data                   = "${file("files/odc1.sh")}"

  #root_block_device {
     #volume_size = "30"
     #volume_type = "standard"
  #}
}
