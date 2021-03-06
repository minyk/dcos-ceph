package com.mesosphere.sdk.ceph.api.controller;

import com.mesosphere.sdk.api.ResponseUtils;
import com.mesosphere.sdk.ceph.api.util.CephEtcdClient;
import org.slf4j.Logger;
import org.slf4j.LoggerFactory;

import javax.ws.rs.GET;
import javax.ws.rs.Path;
import javax.ws.rs.Produces;
import javax.ws.rs.core.Response;

/**
 * REST API for ceph.conf.
 */
@Path("/v1/ceph/config")
public class CephConfigController {
    private final Logger log = LoggerFactory.getLogger(CephConfigController.class);
    private CephEtcdClient cephetcdclient;

    public CephConfigController(CephEtcdClient client) {
        this.cephetcdclient = client;
    }

    @GET
    @Path("/ceph.conf")
    @Produces("plain/text")
    public Response getConfig() {
        try {
            log.info("Getting ceph config from etcd.");
            return ResponseUtils.plainOkResponse(
                    cephetcdclient.getGlobalConf()
                            + cephetcdclient.getMonitorConf()
                            + cephetcdclient.getOSDConf()
                            + cephetcdclient.getMDSConf()
                            + cephetcdclient.getClientConf()
            );
        } catch (Exception e) {
            log.error("Fail to get configuration from etcd: {}", e.getMessage());
            return Response.serverError().build();
        }
    }
}
