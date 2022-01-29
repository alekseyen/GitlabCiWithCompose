# -*- mode: ruby -*-
# vi: set ft=ruby :

# if need run ssh by private_key uncoment 60-62, 75-79

require 'etc'

@ip1 = "10.211.0.101"
@ip2 = "10.211.0.102"

puts "This script will start these VMs:"
puts "%s-node1 with IP %s" % [Etc.getlogin, @ip1]
puts "%s-node2 with IP %s" % [Etc.getlogin, @ip2]
# puts "%s-node3 with IP %s" % [Etc.getlogin, @ip3]

$update_ubuntu = <<SCRIPT
sudo apt-get update
sudo apt-get install python-dev python3-dev -y
SCRIPT

$update_centos = <<SCRIPT
sudo yum -y install python-devel python3-devel
SCRIPT

Vagrant.configure("2") do |config|
  config.hostmanager.enabled = false
  config.hostmanager.include_offline = true
  config.hostmanager.ignore_private_ip = false
  config.ssh.forward_agent = true

  config.vm.define :node1 do |node1|
    node1.vm.box = "ubuntu/bionic64"
    node1.vm.provider "virtualbox" do |vb|
      vb.cpus = "1"
      vb.memory = "1024"
    end
    node1.vm.network :private_network, ip: @ip1
    node1.vm.hostname = Etc.getlogin + "-node1"
    node1.vm.provision :hostmanager
    node1.vm.provision :shell, :inline => $update_ubuntu
#     node1.vm.provision "file", source: "~/.ssh/tpos.pub", destination: "~/.ssh/me.pub"
    node1.vm.provision :shell, inline: <<-SHELL
      sed -i 's/PasswordAuthentication no/PasswordAuthentication yes/g' /etc/ssh/sshd_config
      sudo service ssh restart
    SHELL
#     node1.vm.provision "shell", inline: <<-SHELL
#       cat /home/vagrant/.ssh/me.pub >> /home/vagrant/.ssh/authorized_keys
#     SHELL
  end

  config.vm.define :node2 do |node2|
    node2.vm.box = "ubuntu/trusty64"
    node2.vm.provider "virtualbox" do |vb|
      vb.cpus = "1"
      vb.memory = "1024"
    end
    node2.vm.network :private_network, ip: @ip2
    node2.vm.hostname = Etc.getlogin + "-node2"
    node2.vm.provision :hostmanager
    node2.vm.provision :shell, :inline => $update_ubuntu
#     node2.vm.provision "file", source: "~/.ssh/tpos.pub", destination: "~/.ssh/me.pub"
    # for ssh access using local public key
#     node2.vm.provision "shell", inline: <<-SHELL
#       cat /home/vagrant/.ssh/me.pub >> /home/vagrant/.ssh/authorized_keys
#     SHELL
    node2.vm.provision :shell, inline: <<-SHELL
      sed -i 's/PasswordAuthentication no/PasswordAuthentication yes/g' /etc/ssh/sshd_config
      sudo service ssh restart
    SHELL
  end
end