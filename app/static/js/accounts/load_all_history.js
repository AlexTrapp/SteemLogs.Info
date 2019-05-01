function LoadAllHistory() {
  var load_account_history_url = $(".CSEntriesList").data(
    "ax-load-account-history-url"
  );

  $.ajax({
    url: load_account_history_url,
    type: "GET",
    processData: false,
    contentType: false,
    timeout: 0,
    success: function(response) {
      if (response.action !== "load") {
        $(".CSLoadPostsButton").show();
        $(".CSLoadPostsButton").addClass("enabledLoad");
        $(".CSLoadAllPostsButton").show();
        $(".CSLoadAllPostsButton").addClass("enabledLoad");
        $(".CSLoadHistoryButton").show();
        return;
      }

      $(".CSEntriesList").empty();
      $(".CSEntriesList").append(response.content);
      $(".CSAccountLoadPostsSpinner").hide();

      // Check applied tags to filter
      var tags_list = [];
      $(".applied_tag_filters li").each(function(i, obj) {
        tags_list.push($(obj).data("tag"));
      });

      // Check applied title search
      var search_text = $("#id_title_search_field")
        .val()
        .toLowerCase();

      $(".CSEntriesList tr").each(function(i, obj) {
        var hide_by_tag = false;

        for (var tag_idx in tags_list) {
          if ($(obj).hasClass(tags_list[tag_idx]) == false) {
            hide_by_tag = true;
          }
        }

        if (hide_by_tag == true) {
          $(obj).hide();
        }

        var title = $(obj)
          .data("entry-title")
          .toLowerCase();

        if (search_text) {
          if (!title.includes(search_text)) {
            $(obj).hide();
          }
        }
      });
    }
  });
}

$(function() {
  "use strict";

  $(".CSLoadHistoryButton").on("click", function() {
    $(this).hide();
    $(".CSLoadPostsButton").hide();
    $(".CSLoadAllPostsButton").hide();
    $(".CSAccountLoadPostsSpinner").show();
    LoadAllHistory();

    return;
  });
});
