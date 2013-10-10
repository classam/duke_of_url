package "python-pip"
package "python-dev"

execute "pip install netifaces" do
    command "pip install netifaces"
    user "root" 
end
