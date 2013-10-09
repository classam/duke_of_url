directory "/var/chef" do
    owner "vagrant"
    action :create
end

directory "/var/chef/cache" do
    owner "vagrant"
    action :create
end
