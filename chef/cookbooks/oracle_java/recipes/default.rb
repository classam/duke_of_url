package "python-software-properties" 

execute "add ppa" do
    command "add-apt-repository ppa:webupd8team/java"
    user "root"
end
execute "update" do
    command "apt-get update"
    user "root"
end
execute "accept license terms" do
    command "echo oracle-java7-installer shared/accepted-oracle-license-v1-1 select true | /usr/bin/debconf-set-selections"
    user "root" 
end

package "oracle-java7-installer"
package "oracle-java7-set-default" 
    
