'''
 rmtoo
   Free and Open Source Requirements Management Tool
   
  Constraints handling
   
 (c) 2010-2012 by flonatel GmbH & Co. KG

 For licensing details see COPYING
'''

from rmtoo.lib.logging.EventLogging import tracer

# pylint: disable=W0232
class Constraints:

    @staticmethod
    def set_default_values(cfg):
        cfg.set_value('constraints.search_dirs',
                      ['/usr/share/pyshared/rmtoo/collection/constraints'])

    @staticmethod
    def collect(topic_set):
        '''Collect all the constraints which are used in the given topic.'''
        tracer.debug("Called for topic set.")
        cnsts = {}
        
        if topic_set == None:
            assert False
        
        for ctr, cval in topic_set.get_requirement_set().get_constraints().iteritems():
            tracer.debug("Add constraint [%s]" % ctr)
            cnsts[ctr] = cval
        tracer.debug("Finished; size [%d]" % len(cnsts))
        return cnsts
