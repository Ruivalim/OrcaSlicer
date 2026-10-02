# src/slic3r/plugin/CloudPluginService.hpp

- OrcaCloudServiceAgent · class · L14-L14 — class OrcaCloudServiceAgent;
- CloudPluginDownload · class · L16-L19 — struct CloudPluginDownload
- CloudPluginService · class · L21-L43 — class CloudPluginService
- set_cloud_agent · function · L24-L24 — void set_cloud_agent(std::shared_ptr<OrcaCloudServiceAgent> agent);
- get_cloud_agent · function · L25-L25 — std::shared_ptr<OrcaCloudServiceAgent> get_cloud_agent() const;
- can_fetch_cloud_plugins · function · L26-L26 — bool can_fetch_cloud_plugins() const;
- fetch_manifests_into_descriptors · function · L27-L29 — bool fetch_manifests_into_descriptors(std::vector<PluginDescriptor>& descriptors,
- request_cloud_subscribe · function · L30-L30 — bool request_cloud_subscribe(const std::string& plugin_uuid, std::string& error) const;
- request_cloud_unsubscribe · function · L31-L31 — bool request_cloud_unsubscribe(const PluginDescriptor& plugin, std::string& error) const;
- download_cloud_plugin · function · L32-L35 — bool download_cloud_plugin(PluginDescriptor& entry,
- fetch_plugin_changelog · function · L36-L36 — bool fetch_plugin_changelog(const PluginDescriptor& descriptor, std::vector<PluginChangelog>& changelog, std::string& error) const;
- fetch_plugin_changelog · function · L37-L39 — bool fetch_plugin_changelog(const std::vector<PluginDescriptor>& descriptors,
