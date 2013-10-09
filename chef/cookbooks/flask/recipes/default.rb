package "python-pip"

execute "pip install flask" do
    command "pip install flask"
    user "root" 
end
