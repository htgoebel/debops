Getting started
===============

.. contents::
   :local:


Default configuration
---------------------

The configuration is split into 3 basic parameters,
this is because of limitation of YAML and easier representation.

- ejabberd__*_config_global
- ejabberd__*_config_components
- ejabberd__*_config_virtual_hosts

By default there are two components active
:envvar:`ejabberd__http_upload` and :envvar:`ejabberd__muc`. Set this
varables to false to disable the specific component.

Domains
~~~~~~~

The default virtual host uses :envvar:`ejabberd__domain` as domain.

The components uses two subdomains: conference.`ejabberd__domain` and
upload.`ejabberd__domain`.

Ports
~~~~~

By default the ports are:
- `5222` (client-to-server, c2s-tls)
- `5223` (client-to-server ofer TLS, c2s-tls)
- `5269` (server-to-server, s2s)
- `5270` (server-to-server over TLS, s2s-tls)
- `5280` http (only used when XXX behind a nginx server)
- `5281` https  (used when `not` XXX behind a nginx server)



Example inventory
-----------------

To enable Ejabberd server support on a host, it needs to be included
in the Ansible inventory in a specific group:

.. code-block:: none

   [debops_service_ejabberd]
   hostname

Example playbook
----------------

If you are using this role without DebOps, here's an example Ansible
playbook that uses the ``debops.ejabberd`` role:

.. literalinclude:: ../../../../ansible/playbooks/service/ejabberd.yml
   :language: yaml


Ansible tags
------------

You can use Ansible ``--tags`` or ``--skip-tags`` parameters to limit
what tasks are performed during Ansible run. This can be used after a
host was first configured to speed up playbook execution, when you are
sure that most of the configuration is already in the desired state.

Available role tags:

``role::ejabberd``
  Main role tag, should be used in the playbook to execute all of the role
  tasks as well as role dependencies.

``role::ferm``
  Role tag for configure the firewall ferm.
