import { Template } from 'meteor/templating';
import { ReactiveVar } from 'meteor/reactive-var';

import './main.html';

Template.presenca.onCreated(function presencaOnCreated() {
  // counter starts at 0
  this.counter = new ReactiveVar(0);
  EthBlocks.init();
});

Template.presenca.helpers({
  counter() {
    return Template.instance().counter.get();
  },
  currentBlock() {
      return EthBlocks.latest.number;
  }
});

Template.presenca.events({
  'click button'(event, instance) {
    // increment the counter when button is clicked
    instance.counter.set(instance.counter.get() + 1);
  },
});
