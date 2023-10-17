def igmp_snooping_groups(self,  hdl, vlan ):
    cmd = ' show ip igmp snooping groups vlan {0} '.format(vlan)
    output = hdl.execute(cmd)
    log.info (output)
    cmd = ' show ip igmp snooping groups vlan {0} | json-pretty'.format(vlan)
    output = hdl.execute(cmd)
    log.info (output)
    temp = 0

    try:
        output_json = json.loads(output)
    except Exception as e:
        log.info("Invalid Json output : "+str(e))
        temp = 1
    if temp == 0 and type(output_json) is dict:
        return output_json
    else:
        return ""
